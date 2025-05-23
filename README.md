# 🗣️ English Accent Detection App

This Streamlit app detects the **English accent** of a speaker from a  public video URL (e.g., Google Drive or direct .mp4 link). It uses audio transcription and a language model (Mistral) to classify the accent and provide a confidence score and short explanation.

## Features

- Accepts public Google Drive links or direct MP4 video URLs
- Downloads the video and extracts audio
- Transcribe English speech using Faster Whisper
- Detect accent (e.g., Indian, American, British, etc.) using the Mistral API
- Return accent type,confidence score and a short explanation
- Simple and interactive web UI built with Streamlit

## Tech Stack

- Streamlit — Web interface
- Faster Whisper — Local speech transcription
- MoviePy — Audio extraction
- gdown — Google Drive download helper
- Mistral API — For accent detection

## How to Use

- Paste a public Google Drive link
OR a direct .mp4 URL.
- Click "Analyze Accent"
- The app will:
- Download the video
- Extract the audio
- Transcribe the English speech
- Detect the speaker’s accent
- View the result as JSON (accent type, confidence, and explanation)

## Notes
- supported format1:Google Drive: https://drive.google.com/file/d/FILE_ID/view
- supported format2:Direct MP4: https://github.com/youruser/yourrepo/raw/main/video.mp4
- Supports English speech only.
- Transcription runs locally on CPU with Whisper (base).
