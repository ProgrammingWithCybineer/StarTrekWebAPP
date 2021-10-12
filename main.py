# this project i want to be able to ask the "Computer" a question
# and in the computer voice form star trek TNG it give me an answer
# Code will use different voices to answer different questions

import os
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS


name = ""

#need a way for the computer to tell what type of question you are asking
def speak(text):
    tts = gTTS(text = text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)


#need a way for the computer to know you are asking a question:
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


speak("Hello, What is your name?")
text = get_audio()

# trying to get code to save users name for future use within the code when asking questions to the assistant 8/27/21






#if "hello" in text:
#    speak("hello, how are you?")

#if "what is your name" in text:
 #   speak("My name is Cybineer")


#speak("Hello Selena")
#get_audio()



#need a API for the computer to use to get the best possible answer to your question
# using googles API







#need a way to get charaters voice to be used in voicing answer to questions






