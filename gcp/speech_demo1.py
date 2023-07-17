import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = '../creds/sa_speech_demo.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# Load the audio into memory
audio_file = '../data/61-70968-0003.flac'
with io.open(audio_file, 'rb') as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

# configure for .flac file
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=16000,
    language_code="en-US",
)

response = client.recognize(config=config, audio=audio)
print(response.results[0].alternatives[0].transcript)