# Flask-Application-Development-for-Speech-Recognition

## What is Flask ?

Flask is an API of Python that allows us to build web-applications in a very easy and friendly way. It is a web-application framework which is based on WSGI (Web Server Gateway Interface) toolkit and Jinja2 template engine. Read more about flask from [here](https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/).

## What is Speech Recognition ?

Speech Recognition is a technique where we can convert or transcribe or recognize speech into its corresponding text. We can use various python libraries to do that. Some of the libraries are SpeechRecognition, deepspeech, google-cloud-speech, watson-developer-cloud, wit, etc. You can look at [this](https://realpython.com/python-speech-recognition/) and [this](https://searchcustomerexperience.techtarget.com/definition/speech-recognition) website to know more about the speech recognition. It really helped me in understanding the concept and the workings behind these libraries.  

## Speech to Text Transcription using Flask application

This repository tells you how to develop a flask application for the speech recognition task where you can directly upload any audio file or record your own audio as well to get the transcripted text. I have used SpeechRecognition library to recognize the speech and convert it into text. You can use any library as per your requirements and suitability. You can check this [link](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3) which gives you the step by step process of how to install a Flask Web Application. You can also go through this [github example](https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py) to explore more options to do the speech recognition. 

For the installation of SpeechRecognition library see [this](https://pypi.org/project/SpeechRecognition/).

## Speech/Audio Analysis

### Number of words per minute

This feature gives us the information about the number of words have been spoken in the audio per minute. From this, we can also gather the speech speed or the rate of speaking per minute. This tells us that whether the person is speaking slowly (if it has less number of words spoken per minute) or the person is speaking fast (if it has high number of words spoken per minute).

### Energy of Audio

The energy of audio tells us the pitch of an audio. This below graph tells us that the intensity of an audio, the high intensity means the audio is clearly audible or in other words it contains some voice whereas low intensity or low energy means the audio doesn't have any voice or it isn't clearly audible. 

![energy graph](https://github.com/ayushirastogi15/Flask-Application-Development/blob/main/static/images/energy.png)

### Filler Words

Filler words are those words which are not properly the words but we use them as fillers in between the sentences while speaking. For example, *right, okay, but, umm, yeah, so, yes...* etc. These words may tell us that whether the person is speaking very fluently or (s)he is using any kind of other words to complete the sentences. Below graph shows us the count of filler words in one of the audio that I've used in this. 

![filler graph]()


