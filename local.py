#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io

from google.cloud import speech_v1p1beta1 as speech

speech_file = 'example.mp3'
# Encoding: https://cloud.google.com/
# speech-to-text/docs/reference/rest/v1beta1/RecognitionConfig
encoding=speech.enums.RecognitionConfig.AudioEncoding.AMR
sample_rate_hertz=8000
# Language: https://cloud.google.com/
# speech-to-text/docs/languages
language_code='en-US'

client = speech.SpeechClient()
with io.open(speech_file, 'rb') as audio_file:
    content = audio_file.read()
audio = speech.types.RecognitionAudio(content=content)
config = speech.types.RecognitionConfig(
    encoding=encoding,
    sample_rate_hertz=sample_rate_hertz,
    language_code=language_code,
    # Enhanced models are only available to projects that
    # opt in for audio data collection.
    use_enhanced=True,
    # A model must be specified to use enhanced model.
    model='phone_call',
    profanity_filter=False,
    enable_automatic_punctuation=True,
    enable_word_confidence=True)
response = client.recognize(config, audio)
for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print('-' * 20)
    print('First alternative of result {}'.format(i))
    print('Transcript: {}'.format(alternative.transcript))
