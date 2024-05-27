import whisper
import sounddevice as sd
import numpy as np
import requests
import os
from dotenv import load_dotenv

load_dotenv()

model = whisper.load_model("base")

# Transcribe the audio which consist of ENGLISH and SIMPLIFIED CHINESE ONLY, Make sure to transcribe each word as it is spoken and not convert it to another language
#     English words should be transcribed in English, and Chinese words should be transcribed in SIMPLIFIED Chinese. 
#     For example, if the spoken sentence is '你好，I went to work,' the transcription should be '你好，I went to work.' 
#     Ensure accuracy in capturing both languages, and be attentive to mixed-language sentences!!!!!
  # "initial_prompt": """Make sure to transcribe each word as it is spoken and not convert it to another language. 
  # So english words to english and chinese words to simplified chinese."""

options = {
    # "language": "zh",  # Primary language, or set to None for automatic detection
    "initial_prompt": """Make sure to NEVER transcribe each word to another language. ONLY TRANSCRIBE ENGLISH AND SIMPLIFIED CHINESE.
   So ENGLISH words to ENGLISH and chinese words to SIMPLIFIED CHINESE.""",
}

def transcribe_audio(audioPath):
  result = model.transcribe(audioPath, **options)
  # files = { 'file': (audioFile.filename + '', open(audioPath, 'rb'), audioFile.content_type)}
  # response = requests.post(os.getenv('BACKEND_API') + '/uploadAudioFile', 
  #                          files=files, 
  #                          json={ "message": result})
  return result
