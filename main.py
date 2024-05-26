from fastapi import FastAPI, Request, File, UploadFile
from typing import Annotated
from Speech2Text import transcribe_audio
from LLM import llm_run
import uvicorn
import os
import shutil

app = FastAPI()

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)

@app.post("/speech2text")
async def transcribe(file: UploadFile):
  file_path = os.path.join('./', "audio.m4a")
    
  with open(file_path, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)

  return { "words": transcribe_audio("./audio.m4a") }

@app.post("/generateResponse")
async def generate_response(request: Request):
  request = await request.json()  # Parse the JSON body
  latestMessages = request['input']
  response = llm_run(latestMessages)
  return { "your question": latestMessages,
          "reply": response }

# @app.post("/text2speech")
# async def text2speech(request: Request):
#   request = await request.json()
#   return { "response": text_2_speech(request['input']) }