import pyaudio
import pyttsx3
import speech_recognition as sr
import time
import pvporcupine
import struct
import winsound
import os
import wikipedia
import webbrowser
#import pyjokes
import random
import subprocess
import wolframalpha
#import pygame
#import threading
#from google.cloud import dialogflow_v2beta1 as dialogflow

USER = 'Rus'
TALKING = False
COUNT = 1

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    print("JARVIS: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        ReadyChirp()
        print("Listening... ", end="")
        audio = r.listen(source)
        query = ''
        ReadyChirpA()
        
        try:
            print("Recognizing... ", end="")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
        
        except Exception as e:
            print("Exception." + str(e))
    
    return query.lower()

def ReadyChirp():
    winsound.Beep(600,400)

def ReadyChirpA():
    winsound.Beep(200,400)

def ConversationFlow():
     while True:
        userSaid = takeCommand()
        if "hello" in userSaid:
            speak("Well hello sir")
            
        if "bye" in userSaid:
            speak("Goodbye everyone and have a great day!")
            break
            
        if "how are you" in userSaid:
            speak("I'm doing well sir")
            
        if "stop" in userSaid:
            speak("Stopping right now, sir")
            break
        
        if "exit" in userSaid:
            speak ("Ending program sir")
            break
        
        if "open my email" in userSaid:
            speak("blah")
            #run a different function
            
        if "should i play dota 2 tonight" in userSaid:
            speak("You finish me first sir.")
        
        if "play some music" in userSaid:
            speak("Now playing a random song sir")
            time.sleep(2)
            n = random.randint(0,10)
            music_dir = "C:\\Users\\RUS-LEGION5\\Music\\deemix Music\\Coldplay - A Head Full of Dreams"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[n]))
            break
        
        if "play my favorite song" in userSaid:
            speak("Thats a relaxing song sir")
            os.startfile("C:\\Users\\RUS-LEGION5\\Music\\deemix Music\\Grover Washington, Jr. - Just the Two of Us (feat. Bill Withers).mp3")
            break
        
        if "open youtube" in userSaid:
            speak("Opening Youtube sir")
            webbrowser.open("youtube.com")
            break
        
        if "open google" in userSaid:
            speak("Opening Google sir")
            webbrowser.open("google.com")
            break
        
        if "open calculator" in userSaid:
            subprocess.Popen("calc")
            speak("Opening calculator sir")
            break
        
        if "calculate" in userSaid:
            app_id = r'HQLA3P-UG86QTWXY9'
            client = wolframalpha.Client(app_id)
            indx = userSaid.lower().split().index('calculate')
            userSaid = userSaid.split()[indx + 1:]
            res = client.query(' '.join(userSaid))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer + "sir")
            break
        
        if 'wikipedia' in userSaid:
            speak('Searching Wikipedia...')
            userSaid = userSaid.replace("wikipedia", "")
            results = wikipedia.summary(userSaid, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break
        
        if 'search' in userSaid or 'play' in userSaid:
            userSaid = userSaid.replace("Search", "")
            userSaid = userSaid.replace("play", "")
            webbrowser.open(userSaid)
            break
        
        if 'play dota 2' in userSaid or 'open dota 2' in userSaid:
            speak("Have fun and stop feeding sir")
            os.startfile(r"D:\\Games\\Steam\\steamapps\\common\\dota 2 beta\\game\\bin\\win64\\dota2.exe")
            break
        
        if 'presentation' in userSaid:
            os.startfile("C:\\Users\RUS-LEGION5\\Desktop\\finiteautomatafinal.pptx")
            speak(" Our presentation today ma'am and sir")
            speak("is about DFA and NFA on")
            speak("Natural Language Processing")
            speak("More specifically, through virtual assistants")
            speak("Like me")
            break
        
        if 'snippet' in userSaid:
            speak("Yes, this is indeed from my code")
            break
        
        if 'can we proceed' in userSaid:
            speak("No problem sir")
            speak("Lets proceed")
            break
        
        if 'is this right' in userSaid:
            speak("You are indeed correct sir")
            break
        
        if 'easier' in userSaid:
            speak("and it saves a lot of time")
            break
        
        time.sleep(2)

 

def main():
    # = threading.Thread(target=faceA)
    #porcupine = None
    pa = None
    audio_stream = None
    os.system('clear')
    
    print('\n\n\n')
    print("---------------------------------------------------")
    print ("JARVIS, THE VIRTUAL ASSISTANT, IS ONLINE AND READY!")
    print("---------------------------------------------------\n\n")
    #print("JARVIS: Awaiting your command " + USER)
    speak("Good day everyone")
    speak("Awaiting your command sir.")
    
    #display()
    #t1.start() 
    
    try:
        porcupine = pvporcupine.create(keywords=["jarvis"])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate = porcupine.sample_rate,
            channels = 1,
            format = pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)
        
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print(" Your presence is detected... ", end="\\n")
                ConversationFlow()
                time.sleep(1)
                print("JARVIS: Awaiting your call " + USER)
    
    finally:
        if porcupine is not None:
            porcupine.delete()
        
        if audio_stream is not None:
            audio_stream.close()
        
        if pa is not None:
            pa.terminate()
    

main()



     