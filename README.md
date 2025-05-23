# 🗣️ English Accent Detection App

This Streamlit app detects the **English accent** of a speaker from a publicly shared **Google Drive video URL**. It uses audio transcription and a language model (Mistral) to classify the accent and provide a confidence score and short explanation.

## Features

- Download video from a public Google Drive link
- Extract audio from the video
- Transcribe English speech using [Faster Whisper](https://github.com/guillaumekln/faster-whisper)
- Detect accent (e.g., Indian, American, British, etc.) using the Mistral API
- Return a confidence score and a short explanation
- Simple and interactive web UI built with Streamlit

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [Faster Whisper](https://github.com/guillaumekln/faster-whisper) (local transcription)
- [MoviePy](https://zulko.github.io/moviepy/) (audio extraction)
- [gdown](https://pypi.org/project/gdown/) (Google Drive download)
- [Mistral API](https://docs.mistral.ai/) (LLM-based accent classification)

## How to Use

- Paste a public Google Drive video URL
- Click "Analyze Accent"
- Wait for:
- Video to download
- Audio to extract
- Speech to transcribe
- Accent to be detected
- View the result as JSON (accent, confidence, and explanation)

## Notes
- Only public Google Drive links work.
- Supports English speech only.
- Transcription runs locally on CPU with Whisper (base).
