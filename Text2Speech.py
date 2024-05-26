from google.cloud import texttospeech
import simpleaudio as sa
from pydub import AudioSegment  
from pydub.playback import play

# Instantiates a client
client = texttospeech.TextToSpeechClient()

def text_2_speech(text):
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=f"{text}")

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="cmn-CN", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    filename = "output.mp3"
    with open(filename, "wb") as out:
        out.write(response.audio_content)

    return

def play_audio(file_path):
    wav_file = AudioSegment.from_file(file=file_path, format="wav")
    play(wav_file)