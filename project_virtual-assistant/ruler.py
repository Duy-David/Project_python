import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

Ruler = pyttsx3.init()
voice = Ruler.getProperty("voices")
Ruler.setProperty("voice", voice[1].id)


def speak(audio):
    print("Ruler: " + audio)
    Ruler.say(audio)
    Ruler.runAndWait()


def time():
    # %i là giờ
    # %m là phút
    # %p: AM || PM
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning, Mr.David")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Mr.David")
    elif hour >= 18 and hour < 24:
        speak("Good Night, Mr.David")

    speak("How can i help you, Boss?")


def command():

    c = sr.Recognizer()
    # with sr.Microphone() as source:
    #     #    thời gian dừng khi ra lệnh
    #     c.pause_threshold = 2
    #     # nghe từ source
    #     audio = c.listen(source)
    try:
        # nhanh6 diện với gg
        print
        # query = c.recognize_google(audio, language="en-US")
        query = str(input("Your order is:"))
        speak("Thanks,boss. This is your oder...")
        print("Phương Duy: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query = str(input("Please repeat or typing the order:"))
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

        elif "open app" in query:
            speak("Which application should I open?")
            app_name = command().lower()
            app_paths = {
                "matketnoi": r"C:\Users\Admin\Desktop\IT\PYTHON\music\matketnoi\dist\matketnoi.exe",
                "mat ket noi": r"C:\Users\Admin\Desktop\IT\PYTHON\music\matketnoi\dist\matketnoi.exe",
                "Mất kết nối": r"C:\Users\Admin\Desktop\IT\PYTHON\music\matketnoi\dist\matketnoi.exe",
            }

            if app_name in app_paths:
                speak(f"Opening {app_name}")
                os.startfile(app_paths[app_name])

            else:
                speak("Application not found. Please try again.")
        elif query in ["Ruler", "hi", "hello"]:
            speak("Hello!.I'm Ruler. How can I assist you today?")

        elif "quit" in query:
            speak("Ruler is quitting sir. Goodbye Boss!")
            quit()
        else:
            speak("Sorry, Boss. I can't help you with this feature.")
