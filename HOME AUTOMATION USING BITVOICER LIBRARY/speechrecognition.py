#!/usr/bin/env python3


# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os

while(1):
    
    


    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.record(source, duration = 2, offset = None)#r.listen(source)
        os.system('flite -t "home automation loaded"')
        WIT_AI_KEY = "TTBZ3CE3S6TF5CWPTFPADCPYX762M3FZ"
        x = r.recognize_wit(audio, key=WIT_AI_KEY)

    # recognize speech using Wit.ai
    # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        print("you said " + x)
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))


    if(x=='light on'):
        
        file=open("relay1.txt","w")
        file.write("ON")
        file.close() 
     

    if(x=='light off'):

        file=open("relay1.txt","w")
        file.write("OFF")
        file.close()

    if(x=='charger on'):
	file.open("relay2.txt","w")
	file.write("ON")
	file.close()

    if(x=="charger off"):
	file.open("relay2.txt","w")
	file.write()
	file.close()
