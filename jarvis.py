import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Please tell me how can i help you sir")
def takeCommand():
     #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
        print("Recoginizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(o,content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('gagana2k@gmail.com','password')
    server.sendmail('gagana2k2gmail.com',to,content)
    server.close


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam,the time is{strtime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Gagana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open my website' in query:
            myweb="C:\\Users\\Gagana\\Desktop\\final front page(websie)"
            os.startfile(myweb)
        elif 'send email' in query:
            try:
                speak("what should i say")
                content=takecommand()
                to="dakshayanibs1974@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry could not send email")