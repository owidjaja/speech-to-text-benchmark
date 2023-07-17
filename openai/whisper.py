import os
import json
import openai

print(os.getcwd())
# import creds
with open('./creds/openai_api.json') as f:
    creds = json.load(f)

openai.api_key = creds['API_KEY']

audio_file = open('./data/ch1.mp3', "rb")
transcript = openai.Audio.transcribe(model="whisper-1",
                                     file=audio_file,
                                     api_key=creds['API_KEY'],
                                     response_format="srt")
print(transcript)

# need to reload file because file is opened as a buffer
audio_file = open('./data/ch1.mp3', "rb")
translate = openai.Audio.translate(model="whisper-1",
                                   file=audio_file,
                                   response_format="srt")
print(translate)

