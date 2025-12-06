import streamlit as st
from functions import generate_story_from_images, narrate_story, extract_title_and_story
from PIL import Image


st.title("AI Story Generator from Images")
st.markdown("Upload 1 to 10 images and let AI craft a unique story based on them!")

with st.sidebar:
    st.header("Controls")
    uploaded_files = st.file_uploader(
        "Upload Images..",
        type=["png", "jpg", "jpeg"], 
        accept_multiple_files=True
    )

    story_style=st.selectbox("Choose Story Genre",
        options=[
            "Fantasy",
            "Science Fiction",
            "Mystery",
            "Romance",
            "Horror",
            "Adventure",
            "Historical",
            "Comedy"
        ])
    generate_button= st.button("Generate Story", type="primary")

if generate_button:
    if not uploaded_files or len(uploaded_files) > 10:
        st.error("Please upload between 1 to 10 images.")
    else:
        image_files = [Image.open(file) for file in uploaded_files]
        st.subheader("Uploaded Images")
        image_cols = st.columns(len(image_files))
        for idx, img in enumerate(image_files):
            with image_cols[idx]:
                st.image(img, use_container_width=True)

        try:
            with st.spinner("Generating story... This may take a moment."):
                story = generate_story_from_images(image_files, story_style)
            
            title, story_content = extract_title_and_story(story)
            
            if not story_content or story_content.strip() == "":
                st.error(f"Failed to extract story content.")
                with st.expander("Debug Info"):
                    st.text(f"Raw response: {story[:500]}")
            else:
                st.title(title)
                st.write(story_content)
                st.success("Story Generated!")

                st.subheader("🎙️ Narrated Story")
                st.markdown("*High-quality text-to-speech narration of your story*")
                with st.spinner("✨ Creating beautiful narration... "):
                    audio_bytes = narrate_story(story_content)
                    if audio_bytes and audio_bytes.getbuffer().nbytes > 0:
                        st.audio(audio_bytes.getvalue(), format="audio/mp3")
                        st.success("Narration ready! Use the player controls to listen.")
                    else:
                        st.warning("Audio generation encountered an issue. The story text might contain unsupported characters.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
