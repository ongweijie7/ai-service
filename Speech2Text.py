import whisper
import sounddevice as sd
import numpy as np
import requests
import os
from dotenv import load_dotenv

load_dotenv()

model = whisper.load_model("base")

options = {
    # "language": "zh",  # Primary language, or set to None for automatic detection
    "initial_prompt": """Make sure to transcribe each word as it is spoken and not convert it to another language. 
    So english words to english and chinese words to simplified chinese."""
}

def transcribe_audio(audioPath):
  result = model.transcribe(audioPath, **options)
  # files = { 'file': (audioFile.filename + '', open(audioPath, 'rb'), audioFile.content_type)}
  # response = requests.post(os.getenv('BACKEND_API') + '/uploadAudioFile', 
  #                          files=files, 
  #                          json={ "message": result})
  return result
