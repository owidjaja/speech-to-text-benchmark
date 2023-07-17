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


# https://stackoverflow.com/questions/29547218/python-split-audio-files-on-silence-and-then-re-encode-each-segment
from pydub import AudioSegment

audio_file_path = "./data/ch1.mp3"
song = AudioSegment.from_mp3(audio_file_path)

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000

first_10_minutes = song[:ten_minutes]

first_10_minutes.export("export.mp3", format="mp3")
