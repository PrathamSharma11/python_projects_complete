from pyttsx3 import engine, speak
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pywhatkit
import datetime
from PyDictionary import PyDictionary as d
import wikipedia
import pyjokes







r=sr.Recognizer()


def speakText(command):  #bolne ka kaam karega
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def dict():
    speak("Activated dictionary!")
    speak("Tell Me The Problem!")
    prob1= Takecom()


    if 'meaning' in prob1:

        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("elon musk","")     
        prob1 = prob1.replace("of","") 
        prob1 = prob1.replace("meaning of","")
        result = d.meaning(prob1)
        speak(f"The Meaning for {prob1} is {result}")
    elif 'synonym' in prob1:

        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("elon musk","")     
        prob1 = prob1.replace("of","") 
        prob1 = prob1.replace("synonym of","")
        result =d.synonym(prob1)
        speak(f"The synonym for {prob1} is {result}")
    elif 'antonym' in prob1:

        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("jarvis","")     
        prob1 = prob1.replace("of","") 
        prob1 = prob1.replace("antonym of","")
        result =d.antonym(prob1)
        speak(f"The synonym for {prob1} is {result}")
        speak("Exited Dictionary!")
        
def Takecom():       #sunne ka kam
    try:
        with sr.Microphone() as b:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(b,duration=0.3)
            #listen to the input from user

            print("i am listening.......")
            audio2 = r.listen(b)
            # using google to recognize audio

            mytext = r.recognize_google(audio2)


            mytext = mytext.lower()

            print(mytext)
            

    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(engine))
    except Exception:         #for error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return mytext
#speakText("hello sir")




def Task():

    def WishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning Pratham Sir!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Pratham Sir!")
        else:
            speak("Good Evening Pratham Sir!")

    def music():
        speak('tell me the name of the song')
        musicname=Takecom()
        if "avicii" in musicname:
            os.startfile('1.mp3')
        else:
            pywhatkit.playonyt(musicname)
        speak("your song has been started, enjoy sir")
    
    def openapps():
        speak("ok sir wait a second")
        
        if 'open media player' in query:
            os.startfile('C:\Program Files (x86)\K-Lite Codec Pack\Media Player Classic\mpc-hc.exe')
        speak("your command has been completed sir.")
        
    def closeapps():
        speak("ok sir wait a second")
        if 'close media player' in query:
            os.system('taskkill/im mediaplayer.exe.format(mediaplayer)')
        elif 'close chrome' in query:
            os.system('TASKKILL /F /im chrome.exe')
        elif 'close youtube' in query:
            os.system('https://www.youtube.com/')



    
    
    WishMe()
    
    
    while True:
        query=Takecom()


        if 'hello elon musk' in query:
            speak("hello Pratham, I am Elon Musk")
            speak("i am your Assistant")
            speak("how may i help you")
        elif 'how are you' in query:
            speak("i am fine")
            speak("what about you")
        elif 'good night' in query:
            speak("good night pratham sir")
        elif 'who am i' in query:
            speak("Your Name is Pratham Sharma")
            speak("you are from Gwalior")
            speak("and you are going to be Very successful, just hustle.")
        elif 'about python' in query:
            speak("Python was created by Guido van Rossum, and first released on February 20, 1991. ")
        
        
        elif 'open youtube' in query:
            speak("ok sir")
            webbrowser.open("https://www.youtube.com/")
            speak("done sir")

        elif 'open gmail' in query:
            speak("ok sir")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("done sir")
        
        elif 'open spotify' in query:
            speak("ok sir")
            webbrowser.open("https://open.spotify.com/")
        
        elif 'open your need' in query:
            speak("Ok sir")
            webbrowser.open("http://urneed.epizy.com/?i=1")
        
        
        elif 'play music' in query:
            music()
        
        elif 'open media player' in query:
            openapps()
        
        elif 'close media player' in query:
            closeapps()
        
        elif 'close chrome' in query:
            closeapps()

        elif 'close youtube' in query:
            closeapps()
        
        elif 'google search' in query:
            speak("this is what i have found for you search, sir")
            query = query.replace("elon musk","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("done sir.")

        elif 'open website' in query:
            speak("tell me the name of the website")
            name = Takecom()
            web ='https://www.' + name + '.com' 
            webbrowser.open(web)
            speak("Done sir")
        
        elif 'dictionary' in query:
            dict()
        
        elif 'close all tab' in query:
            os.system('TASKKILL /F /im chrome.exe')
        
        elif 'shut down' in query:
            pywhatkit.shutdown(time=1)
        
        elif 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("elon musk","")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            

        elif 'joke' in query:
            query = query.replace("elon musk","")
            query = query.replace("tell me a","")
            get = pyjokes.get_joke()
            speak(get)
            



Task()



    



    