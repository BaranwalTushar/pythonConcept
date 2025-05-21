import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests


#pip install pocketsphinx


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "1cb9cb96f65847ba8f2bdff97039bf21"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://goole.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com") 

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]   
        webbrowser.open(link)            

    elif  "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the json response
            data = r.json()

            #Extract the articles
            articles = data.get('articles',[])

            #print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let open ai handle the request.
        pass
        
                    
     
        
        

if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
    
    #Listen for the wake word "jarvis"
    #obtain audio from the microphone

        r = sr.Recognizer()

        print("Recognizing...")
       
        #recognize speech using slice
        try:
          
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word =  r.recognize_google(audio)
            if(word.lower() == "jarvis"):
               speak("Ya")

               #Listen for command

            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                command =  r.recognize_google(audio)


                processCommand(command)

        
        except Exception as e:
         print("Error; {0}".format(e))    
                
            