import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis, How may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('1nh18cs187.sukhmanjeet@gmail.com', '**********')
    server.sendmail('1nh18cs187.sukhmanjeet@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif "open my instagram" in query:
            webbrowser.open("www.instagram.com")
        
        elif "open my facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "play music" in query:
            music_dir = "F:\\Jarvis Project AI\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Now, the time is {strTime}")
        
        elif "send email" in query:
            try:
                speak("what should i type")
                content=takeCommand()
                to = "1nh18cs187.sukhmanjeet@gmail.com"
                sendEmail(to, content)
                speak("email has been sent successfully ")
            except Exception as e:
                # print(e)
                speak("Sorry, system has failed to send the mail")




        


        






    
