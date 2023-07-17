# Automatic Speech Recognition Demos

## Dataset
- [LibriSpeech](http://www.openslr.org/12/)
- [FLEURS](https://huggingface.co/datasets/google/fleurs)

## GCP Speech-to-Text
- [Jie Jenn](https://www.youtube.com/watch?v=izdDHVLc_Z0)

## AWS Transcribe


## OpenAI-Whisper
- [Jie Jenn](https://www.youtube.com/watch?v=BkcSJol59Rg)

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
