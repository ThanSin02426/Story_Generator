# AI Story Generator from Images

Turn your images into captivating stories with AI-powered narration!

## You can try 
Fully working link https://storygenerator99.streamlit.app/

## What It Does

Upload 1-10 images, pick a genre, and watch as our AI creates a unique story with professional audio narration.

Well this web app has an amazing thing, that it takes helps of Ai to write prompt and then feeds it back to Ai creating a cool loop. 

## Quick Start

### 1. Setup
```bash
python3 -m venv streamenv
source streamenv/bin/activate
pip install -r requirements.txt
```

### 2. Configure
Create a `.env` file:
```
GOOGLE_API_KEY=your_key_here
```

### 3. Run
```bash
streamlit run app.py
```

## How to Use

1. Upload your images (PNG, JPG, JPEG)
2. Choose a story genre (Fantasy, Sci-Fi, Mystery, etc.)
3. Click "Generate Story"
4. Read your story and listen to the audio narration

## What You'll Get

- ✨ Unique AI-generated stories based on your images
- 🎙️ High-quality audio narration
- 📖 Clean, readable story format with titles
- ⚡ Fast generation (under 2 minutes)

## File Structure

```
├── app.py          # Main app
├── functions.py    # Core logic
├── requirements.txt
└── .env           # Your API key (don't share!)
```

## Getting Your API Key

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project and enable Generative AI API
3. Generate an API key
4. Add it to `.env`

## Supported Genres

Fantasy • Sci-Fi • Mystery • Romance • Horror • Adventure • Historical • Comedy

## Troubleshooting

**Audio won't generate?** - Check your internet connection or try a shorter story

**Story generation fails?** - Verify your API key and image formats

**Getting import errors?** - Reinstall: `pip install -r requirements.txt`

## Made With

- [Streamlit](https://streamlit.io/) - Web framework
- [Google Gemini AI](https://ai.google.dev/) - Story generation
- [gTTS](https://gtts.readthedocs.io/) - Audio narration

---

**Ready to create?** Run `streamlit run app.py` and start uploading! 🚀

