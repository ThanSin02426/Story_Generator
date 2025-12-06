from dotenv import load_dotenv
import os
from google import genai
from gtts import gTTS
import io
from io import BytesIO

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    raise ValueError("API_KEY environment variable not set")

client = genai.Client()

def create_advanced_prompt(story_style, image_files):
    prompt = f"Based on these images, create a {story_style} story. Format your response EXACTLY like this:\n\nTitle: [Your Story Title]\n\n[The story content here]"
    return prompt


def generate_story_from_images(image_files, story_style):
    prompt = f"Based on these images, create a LONG and detailed {story_style} story with interesting characters and plot twists. The story should be at least 500 words. Format your response EXACTLY like this:\n\nTitle: [Your Story Title]\n\n[The complete story content here - make it long and detailed]"
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[image_files, prompt]
    )
    return response.text

def extract_title_and_story(story_text):
    text = story_text.strip()
    
    if "Title:" in text:
        parts = text.split("Title:", 1)
        if len(parts) > 1:
            remaining = parts[1].strip()
            title_line = remaining.split('\n', 1)[0].strip()
            title = title_line.replace('**', '').replace('*', '').replace('#', '').strip()
            story_content = remaining.split('\n', 1)[1].strip() if '\n' in remaining else ""
            story_content = clean_text_for_narration(story_content)
            return title, story_content
    
    lines = text.split('\n')
    title = lines[0].replace('**', '').replace('*', '').replace('#', '').strip() or "Untitled Story"
    story_content = '\n'.join(lines[1:]).strip()
    story_content = clean_text_for_narration(story_content)
    return title, story_content

def clean_text_for_narration(text):
    text = ' '.join(text.split())
    import re
    text = re.sub(r'([.!?])\s+', r'\1 ', text)
    text = text.strip()
    return text

def narrate_story(story_text, lang='en'):
    try:
        text_to_narrate = story_text[:2500]
        tts = gTTS(
            text=text_to_narrate, 
            lang=lang, 
            slow=False,
            tld='com',
        )
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
