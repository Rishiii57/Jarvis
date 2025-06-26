import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
import country_converter as coco
from dotenv import dotenv_values

#getting all the API KEYS and other information

secrets = dotenv_values(".env")
newsapi = secrets.get("NEWS_API")
weatherapi = secrets.get("WEATHER_API")
lat = secrets.get("LATITUDE")
lon = secrets.get("LONGITUDE")


aliases = {
    "g": "google",
    "yt": "youtube",
    "fb": "facebook",
    "ig": "instagram",
    "x": "twitter",
    "twt": "twitter",
    "mail": "gmail",
    "r": "reddit",
    "so": "stackoverflow",
    "gh": "github",
    "nf": "netflix",
    "hs": "hotstar",
    "fk": "flipkart",
    "az": "amazon.in",
    "amazon": "amazon.in",
    "wp": "web.whatsapp.com",
    "whatsapp": "web.whatsapp.com",
}

recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open(s):
    url = s[5:]
    url = aliases.get(url, url)
    if '.' in url:
        webbrowser.open("https://" + url)
    else:
        webbrowser.open("https://" + url + ".com")

def play(s):
    song = s[5:]
    if song in musiclib.music:
        webbrowser.open(musiclib.music[song])
        speak(f"Playing {song}!")
    else:
        speak("Sorry, I don't know that song.")

#defining the response to give to the command

def process(c):
    c = c.lower()
    command = c[:4]
    if (command=="open"):
        open(c)
    elif (command=="play"):
        play(c)
    elif "news" in c.lower():
        country = 'USA'
        country_code = coco.convert(country, to="ISO2").lower()

        url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={newsapi}"
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
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weatherapi}&units=metric"
        response = requests.get(url)
        data = response.json()
        speak(f"Temperature {data['main']['temp']} degree celcius ")
        speak(f"Weather {data['weather'][0]['description']}")
        speak(f"Humidity {data['main']['humidity']}%")
        speak(f"Wind Speed {data['wind']['speed']} meter per second")
    else:
        speak("sorry i don't know that command")



#Putting all things together

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