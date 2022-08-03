#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

import flask
import grpc
from flask import Flask
from flask import request
from google.protobuf.json_format import MessageToDict
from pydub import AudioSegment as am

# Load dotenv
from dotenv import load_dotenv
load_dotenv()

# import the generated classes
import stt_service_pb2
import stt_service_pb2_grpc


FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST', "localhost")
FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT', "8000")
FLASK_DEBUG_MODE = True if os.environ.get('FLASK_RUN_PORT') == "development" else False


CONFORMER_HOST = os.environ.get('CONFORMER_HOST', "localhost")
CONFORMER_PORT = os.environ.get('CONFORMER_PORT', "5001")


CHANNEL_IP = f"{CONFORMER_HOST}:{CONFORMER_PORT}"
channel = grpc.insecure_channel(CHANNEL_IP)
stub = stt_service_pb2_grpc.SttServiceStub(channel)
app = Flask(__name__)


def gen(audio_bytes):
    specification = stt_service_pb2.RecognitionSpec(
        partial_results=True,
        audio_encoding='LINEAR16_PCM',
        sample_rate_hertz=16000,
        enable_word_time_offsets=True,
        max_alternatives=5,
    )
    streaming_config = stt_service_pb2.RecognitionConfig(specification=specification)
    yield stt_service_pb2.StreamingRecognitionRequest(config=streaming_config, audio_content=audio_bytes)


def run_transcription(audio_bytes):
    it = stub.StreamingRecognize(gen(audio_bytes))
    try:
        for r in it:
            try:
                jres = MessageToDict(r)
                print(jres)
                if jres['chunks'][0]['final']:
                    return jres['chunks'][0]['alternatives'][0]['text']
            except LookupError:
                print('No available chunks')
    except grpc._channel._Rendezvous as err:
        print('Error code %s, message: %s' % (err._state.code, err._state.details))
    return ""


@app.route("/result", methods=['POST', 'GET'])
def index():
    transcript = ""
    total_time = 0.0
    if request.method == "POST":
        file = request.files['audio_data']

        file.seek(0)

        audio = am.from_file(file)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_sample_width(2)
        audio = audio.set_channels(1)
        
        audio = audio.export(format='wav').read()
        
        start_time = time.time()
        transcript = run_transcription(audio)
        end_time = time.time()
        total_time = end_time - start_time

    response = flask.jsonify({'cfm': {'transcript': transcript, 'time': round(total_time, 2)}})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    app.run(host=FLASK_RUN_HOST, port=FLASK_RUN_PORT, debug=FLASK_DEBUG_MODE)
