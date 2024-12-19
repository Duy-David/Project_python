import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty("voices")
friday.setProperty("voice", voice[1].id)


def speak(audio):
    print("F.R.I.D.A.Y: " + audio)
    friday.say(audio)
    friday.runAndWait()


def time():
    # %i là giờ
    # %m là phút
    # %p: AM || PM
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir.David")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir.David")
    elif hour >= 18 and hour < 24:
        speak("Good Night Sir.David")

    speak("how can i help you?")


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        #    thời gian dừng khi ra lệnh
        c.pause_threshold = 2
        # nghe từ source
        audio = c.listen(source)
    try:
        # nhanh6 diện với gg
        query = c.recognize_google(audio, language="en-US")
        print("Phương Duy: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query = str(input("Your order is:"))
    return query


if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("what should I search Boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"here is your {search} on google")
        if "youtube" in query:
            speak("what should I search Boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"here is your {search} on youtube")
        elif "open video" in query:
            video = (
                r"C:\Users\Admin\Desktop\IT\PYTHON\project_virtual-assistant\test.mp4"
            )
            os.startfile(video)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Friday is quitting sir. Goodbye Boss!")
            quit()
