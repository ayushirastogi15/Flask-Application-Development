# Importing required libraries.

from flask import Flask, render_template, request, Response, redirect, url_for
from werkzeug.utils import secure_filename
from pydub import AudioSegment
import subprocess
import matplotlib.pyplot as plt
import speech_recognition as sr
import numpy as np
import os, io
import wave
#import pyaudio
import math
import scipy.io.wavfile

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')
	

@app.route('/', methods = ['GET', 'POST'])
def uploaded_file():
    transcript = ""
    wpm = ""
    dst = "audio.wav"

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        f = request.files['file']
        #print(type(f), f)
        if f.filename == "":
            return redirect(request.url)

        #print(f.filename, ".mp3" in f.filename)
        if ".mp3" in f.filename:
            # convert mp3 to wav                                                        
            sound = AudioSegment.from_mp3(f.filename)
            sound.export(dst, format="wav")

        elif "recorded_audio" in f.filename:
            subprocess.call(['ffmpeg', '-i', f.filename, dst])

        else:
            f.save(secure_filename(f.filename))
            #transcript = speechtotext(f.filename)
            dst = f.filename
        
        transcript = speechtotext(dst)
        duration = read_wav_file(dst)
        wpm = math.ceil((len(transcript.split(' '))/duration)*60)
        filler_word = filler_words(transcript)

        #print("Duration of audio : ", duration)
        #print("#words in audio : ", len(transcript.split(' ')))
        #print("Words per minute : ", wpm)
        #print("Number of filler words : ", filler_word)

        plot = plot_fillers(filler_word)
        energy = plot_energy(dst)        

    return render_template('upload.html', transcript=transcript, wpm=wpm, name=plot, energy=energy)

def read_wav_file(filename):
    with wave.open(filename, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        #buffer = w.readframes(frames)
        dur = frames/float(rate)
    #print(rate)

    return dur           #buffer, rate

def speechtotext(filename):
    # use the audio file as the audio source                                        
    rec = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = rec.record(source)  # read the entire audio file                  
        transcript = rec.recognize_google(audio)

        #print("Transcription: " + transcript)

    return transcript

def filler_words(text):
    filler_words_list = ['well', 'um', 'umm', ' er', 'uh', 'ah', 'hmm', 'like', 'actually', 'basically',
    'seriously', 'totally', 'literally', 'clearly', 'you see', 'you know', 'i mean', 'you know what i mean',
    'at the end of the day', 'believe me', 'i guess', 'i suppose', 'or something', 'okay', 'so',
    'right', 'mhm', 'huh', 'anyway', 'as if', 'by the way', 'come on', 'definitely', 'do you mean to say',
    "don't tell me", 'however', 'i know', 'i see', 'if you say so', 'in fact', 'incidentlly',
    'meanwhile', 'never', 'no way', 'not a chance', 'not at all', 'of course', 'oh! i see',
    'oh! sure', 'by all means', 'surely', 'certainly', 'precisely', 'so what', 'tell me', 'well',
    'wow', 'ok' ]

    fillers = {}
    text = text.lower()

    for w in filler_words_list:
        if w in text:
            fillers[w] = text.count(w)
   
    return fillers

def plot_fillers(num_filler):
    key = []
    val = []

    for k, v in num_filler.items():
        key.append(k)
        val.append(v)
    
    plt.figure(1)
    plt.barh(key, val)
    if key:
        plt.title("Graph of fillers in audio transcript")
    else:
        plt.title("No fillers in audio")
    plt.xlabel("Count of filler")
    plt.ylabel("Fillers")
    plt.savefig('flask_env/static/images/plot.png')
    #plt.show()
    
    return "plot.png"

def plot_energy(file):

    # Extract Raw Audio from Wav File
    spf = wave.open(file, "r")
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "Int16")
    rate = spf.getframerate()
    num_channel = spf.getnchannels()

    #print("fs : ", rate)
    #print("num of channels : ", spf.getnchannels())
    #print("spf : ", spf)
    #print("signal : ", signal, "shape : ", signal.shape)
    #print("energy : ", np.sum(signal.astype(float)**2))

    Time = np.arange(0, float(len(signal)), 1) / rate / num_channel
    #print("time : ", Time)
    
    plt.figure(2)
    plt.title("Energy of audio ")
    plt.xlabel("Time (sec)")
    plt.ylabel("Energy Signals ")
    plt.plot(Time, signal, linewidth=0.06, alpha=1, color='#ff7f00')
    plt.savefig("flask_env/static/images/energy.png")
    #plt.show()

    return "energy.png"    

if __name__ == '__main__':
    app.run(debug=True)


