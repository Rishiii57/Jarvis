import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
from dotenv import dotenv_values

secrets = dotenv_values(".env")

recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = secrets.get("NEWS_API")
weatherapi = secrets.get("WEATHER_API")
lat = secrets.get("LATITUDE")
lon = secrets.get("LONGITUDE")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "open twitter" in c or "open x" in c:
        webbrowser.open("https://twitter.com")
    elif "open gmail" in c:
        webbrowser.open("https://mail.google.com")
    elif "open reddit" in c:
        webbrowser.open("https://reddit.com")
    elif "open stackoverflow" in c:
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c:
        webbrowser.open("https://github.com")
    elif "open whatsapp" in c:
        webbrowser.open("https://web.whatsapp.com")
    elif "open netflix" in c:
        webbrowser.open("https://netflix.com")
    elif "open hotstar" in c:
        webbrowser.open("https://hotstar.com")
    elif "open amazon" in c:
        webbrowser.open("https://amazon.in")
    elif "open flipkart" in c:
        webbrowser.open("https://flipkart.com")
    elif c.lower().startswith("play "):
        song = c[5:]  # remove "play " and take the rest as song name
        if song in musiclib.music:
            webbrowser.open(musiclib.music[song])
            speak(f"Playing {song}")
        else:
            speak("Sorry, I don't know that song.")
    elif "news" in c.lower():
        print("ok news")
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok":
            speak("Here are top three newsheadlines")
            articles = data["articles"][:3]  
            for article in articles:
                speak(article["title"])
        else:
            speak("Breaking news: There is no breaking news.")
    elif("weather" in c.lower()):
        print("ok weather")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weatherapi}&units=metric"
        response = requests.get(url)
        data = response.json()
        speak(f"Temperature {data['main']['temp']} degree celcius ")
        speak(f"Weather {data['weather'][0]['description']}")
        speak(f"Humidity {data['main']['humidity']}%")
        speak(f"Wind Speed {data['wind']['speed']} meter per second")

if __name__ == "__main__":
    speak("Initializing jarvis")

    while True:
        r = sr.Recognizer()
        print("Recognizing speech....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
                command = r.recognize_google(audio)
                print(command)

            if "jarvis" in command.lower() :
                speak("Yes I am here to help")
                
                # Fix: reopen microphone inside this loop
                while True:
                    with sr.Microphone() as source:
                        print("Listening (jarvis active now)....")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        process(command)

        except Exception as e:
            print("Jarvis error: {0}".format(e))