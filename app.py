import os
import requests
import streamlit as st
from moviepy import VideoFileClip
from faster_whisper import WhisperModel
from dotenv import load_dotenv
import gdown

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
#Download video
def download_video(video_url, filename="video.mp4"):
    file_id = video_url.split("/d/")[1].split("/")[0]
    direct_url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(direct_url, filename, quiet=False)
    return filename
#Extract audio
def extract_audio(video_path, audio_path="audio.wav"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    return audio_path
#Transcribe audio
def transcribe_audio(audio_path):
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio_path)
    return " ".join(segment.text for segment in segments).strip()
#Accent Detection
def detect_accent(transcript):
    prompt = f"""
You are a linguistic expert. Given the following transcript from a spoken English interview, identify:

1. The speaker's likely English accent (e.g., American, British, Indian, Australian, etc.)
2. A confidence score (0–100%)
3. A short explanation (max 2–3 sentences)

Transcript:
\"\"\"{transcript}\"\"\"

Respond in this JSON format:
{{
  "accent": "AccentType",
  "confidence": 85,
  "explanation": "Brief explanation here"
}}
"""
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-small",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post("https://api.mistral.ai/v1/chat/completions", json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        return {
    "accent": "Unknown",
    "confidence": 0,
    "explanation": f"Mistral API error: {response.status_code} - {response.text}"
}

# Streamlit UI
st.title("English Accent Detection")
video_url = st.text_input("Enter public Google Drive video URL")

if st.button("Analyze Accent"):
    if video_url:
        with st.spinner("Downloading video..."):
            video_path = download_video(video_url)
        with st.spinner("Extracting audio..."):
            audio_path = extract_audio(video_path)
        with st.spinner("Transcribing..."):
            transcript = transcribe_audio(audio_path)
        st.text_area("Transcript Preview", transcript[:1000])
        with st.spinner("Detecting Accent..."):
            result = detect_accent(transcript)
        st.success("Accent Analysis Result")
        st.json(result)
    else:
        st.error("Please enter a valid video URL.")
