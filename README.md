# Automatic Speech Recognition Demos

## Dataset
- [LibriSpeech](http://www.openslr.org/12/): Common English speech benchmark
- [FLEURS](https://huggingface.co/datasets/google/fleurs): Multilingual speech
- [AMI Meetings](https://huggingface.co/datasets/edinburghcstr/ami): Meeting recordings

## GCP Speech-to-Text
- [Jie Jenn](https://www.youtube.com/watch?v=izdDHVLc_Z0)

## AWS Transcribe


## OpenAI-Whisper API
- [Whisper Overview](https://platform.openai.com/docs/guides/speech-to-text)
- [OpenAI Audio API](https://platform.openai.com/docs/api-reference/audio/create)
- [Jie Jenn](https://www.youtube.com/watch?v=BkcSJol59Rg)

## OpenAI-Whisper Open-Source
- https://github.com/openai/whisper
  - [LibriSpeech](https://colab.research.google.com/github/openai/whisper/blob/master/notebooks/LibriSpeech.ipynb)
  - [Multilingual](https://colab.research.google.com/github/openai/whisper/blob/master/notebooks/Multilingual_ASR.ipynb)
- Community Features:
  - Transcription and diarization (speaker identification)
    - https://github.com/openai/whisper/discussions/264
    - https://colab.research.google.com/drive/1HuvcY4tkTHPDzcwyVH77LCh_m8tP-Qet?usp=sharing
  - Streaming (real-time)
    - https://github.com/openai/whisper/discussions/2
    - https://betterprogramming.pub/color-your-captions-streamlining-live-transcriptions-with-diart-and-openais-whisper-6203350234ef
  - Cpp port (lightweight)
    - https://github.com/ggerganov/whisper.cpp
- Limitation:
  - Hallucination: https://github.com/openai/whisper/discussions/679

## HuggingFace
- [ASR](https://huggingface.co/transformers/model_doc/wav2vec2.html)

## Picovoice
- WER benchmarking
- https://github.com/Picovoice/speech-to-text-benchmark

## Metrics

### Word Error Rate

Word error rate (WER) is the ratio of edit distance between words in a reference transcript and the words in the output
of the speech-to-text engine to the number of words in the reference transcript.

### Real Time Factor

Real-time factor (RTF) is the ratio of CPU (processing) time to the length of the input speech file. A speech-to-text
engine with lower RTF is more computationally efficient. We omit this metric for cloud-based engines.

### Model Size

The aggregate size of models (acoustic and language), in MB. We omit this metric for cloud-based engines.
