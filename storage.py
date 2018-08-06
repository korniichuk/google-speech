#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google.cloud import speech_v1p1beta1 as speech

uri = 'gs://examplebucket/example.mp3'
# Encoding: https://cloud.google.com/
# speech-to-text/docs/reference/rest/v1beta1/RecognitionConfig
encoding='AMR'
sample_rate_hertz=8000
# Language: https://cloud.google.com/
# speech-to-text/docs/languages
language_code='en-US'

client = speech.SpeechClient()
operation = client.long_running_recognize(
        audio=speech.types.RecognitionAudio(uri=uri),
        config=speech.types.RecognitionConfig(
                encoding=encoding,
                sample_rate_hertz=sample_rate_hertz,
                language_code=language_code,
                use_enhanced=True,
                model='phone_call',
                profanity_filter=False,
                enable_automatic_punctuation=True,
                enable_word_confidence=True))
op_result = operation.result()
for result in op_result.results:
    for alternative in result.alternatives:
        print('=' * 20)
        print(alternative.transcript)
        print(alternative.confidence)
