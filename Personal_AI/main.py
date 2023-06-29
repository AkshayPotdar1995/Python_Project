import os
import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import cv2

vid=cv2.VideoCapture(0)


speaker= win32com.client.Dispatch("SAPI.SpVoice")
r=sr.Recognizer()
def takeCommad():
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            print("Recognizing..")
            query=r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            speaker.Speak("Stopping")
            exit()


while True:
    print("Listening...")
    s=takeCommad()
    sites=[["Youtube", "https://youtube.com"], ["google", "https://google.com"]] # You can make as many as possibal list of site
    for site in sites:
        if f"Open {site[0]}".lower() in s.lower():
            speaker.Speak(f"Opening {site[0]}")
            webbrowser.open(site[1])

    SongPath ="C:/Users/ASUS/Downloads/downfall-21371.mp3"  
    if "Open Music".lower() in s.lower():
        speaker.Speak("Opening Music")
        os.startfile(SongPath)


    if "Stop".lower() in s.lower():
        speaker.Speak("Stopping")
        exit()

    if "Date".lower() in s.lower():
        date=datetime.datetime.now().date()
        speaker.Speak(f"date is {date}")

    if "time".lower() in s.lower():
        hour=datetime.datetime.now().hour
        mint=datetime.datetime.now().minute
        speaker.Speak(f"Time is {hour} Hour {mint} Minute")

    if "open eclipse".lower() in s.lower():
        speaker.Speak("Opening Eclipse")
        os.startfile("C:/eclipse/eclipse.exe")







