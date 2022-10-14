import datetime
import json
import os
import webbrowser
from pathlib import Path
from time import sleep
import urllib.request
import cv2
import numpy as np
import pyautogui
import pyjokes as pyjokes
import pyttsx3
import pywhatkit as kit
import speech_recognition as sr
import wikipedia
from urllib.request import urlopen
import smtplib
import requests
from GoogleNews import GoogleNews
import speedtest
from plyer import notification
from bs4 import BeautifulSoup
import cv2


# voice selection for jarvis
from bs4 import BeautifulSoup

googlenews=GoogleNews()
from pygame import mixer
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# voices is a list of voices on your computer
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)


# speak function will take string input and speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# wishMe() function will greet you whenever you run this script
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(" good morning Boss")

    elif hour >= 12 and hour < 18:
        speak(" good afternoon Boss")

    else:
        speak(" Good Evening Boss")

    speak(" I am your assistant JARVIS and how was your day going. Tell me how can i help you?")


# jarvis will take your voice command and convert into string
def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Searching...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said; {query}\n")

    except Exception as e:
        print(e)
        print("Say That Again Please...")
        return "None"

    return query


# jarvis will send email and please make sure to make your gmail account less secure.

def send_email(to, subject, content):
    sender_email = open("email.txt", "r").read( )
    password = open("pass.txt", "r").read()
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    message = f'subject: {subject}\n\n{content}'
    server.sendmail(sender_email, to, message)
    server.close()

def make_request(url):
  response = requests.get(url)
  return response.text


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()
        # Logic for executing tasks based on query

        if 'open wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("open wikipedia", '')
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = open("email.txt", "r").read()
                speak("Subject To Your Email!")
                subject = takeCommand()
                send_email(to, subject, content)
                speak("Email Has been sent Sucessfully!")
            except Exception as e:
                speak("Sorry, there being an error to send email!")
                print(e)

        elif 'open youtube' in query:
            speak('opening youtube..')
            query.replace('open youtube'," ")
            kit.playonyt(query)

        elif'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query:
            pyautogui.press("volumemute")

        elif 'open google' in query:
            go = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(go)


        elif 'open whatsapp' in query:
            speak('opening whatsapp')
            webbrowser.open('web.whatsapp.com')

        elif 'open mobile camera' in query:
            speak('opening mobile camera..')
            webbrowser.open("http://192.168.105.126:8080/")

        elif 'open github' in query:
            speak('opening github..')
            webbrowser.open("github.com")

        elif 'play music' in query:
            DIRECTORY = Path('D:\TAMIL SONGS')
            mixer.init()

            for fp in DIRECTORY.glob('*.mp3'):
                # add each file to the queue
                mixer.music.load(str(fp))
                mixer.music.play()

                # now wait until the song is over
                while mixer.music.get_busy():
                    sleep(1)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")


        elif 'who are you' in query:
            speak('I am JARVIS sir')

        elif 'goodbye' in query:
            speak('goodbye sir')
            exit()

        elif 'take a leave' in query:
            speak('thank you sir')
            exit()

        elif 'music' in query:

            speak("tell me the name of the song!")
            musicName = takeCommand()
            music_dir="D://TAMIL SONGS"
            songs =os.listdir(music_dir)
            for i in songs:
                if i==musicName:
                    os.startfile(os.path.join(music_dir,i))

        elif "headlines" in query:
            speak("getting news for you")
            googlenews.get_news("today news")
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
            speak(a[1:5])

        elif "speed test" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        elif "weather" in query:
            speak("tell me the location")
            search = takeCommand()
            url = f"http://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak((f"current {search} is {temp}"))

        elif "call" in query:
            speak('calling boss')

            from twilio.rest import Client

            account_sid = 'AC8de01cb2d2ff11485290c6e0a1686136'
            auth_token = 'b33ce69285f19b4efb474c246b431be0'

            client = Client(account_sid, auth_token)
            message = client.calls \
                .create(
                twiml='<Response><Say>this is testing call from our call</Say></Response',
                from_='+18022789791',
                to='+919345444811'
            )

        elif "send message" in query:
            speak('what would i say?')
            m=takeCommand()
            from twilio.rest import Client

            account_sid = 'AC8de01cb2d2ff11485290c6e0a1686136'
            auth_token = 'b33ce69285f19b4efb474c246b431be0'

            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=m,
                from_='+18022789791',
                to='+919345444811'
            )
            print(message.sid)
            speak('message has been sent')


        elif "screenshot" in query:
            image = pyautogui.screenshot()
            image.save('screenshot.jpg')
            speak('Screenshot taken.')

        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)

        elif 'covid' in query:
            html_data = make_request('https://www.worldometers.info/coronavirus/')
            # print(html_data)
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            print('total cases : ', total_cases)
            print('new cases', new_cases[1:])
            print('total recovered', total_recovered)
            speak(total_cases)
            speak(new_cases[1:])
            speak(total_recovered)
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
                title="COVID-19 Statistics",
                message=notification_message,
                timeout=5
            )
            speak("here are the stats for COVID-19")

        elif "open camera" in query:
            webcam = cv2.VideoCapture(0)
            sleep(2)
            while True:

                check, frame = webcam.read()
                print(check)  # prints true as long as the webcam is running
                print(frame)  # prints matrix values of each framecd
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    cv2.imwrite(filename='saved_img.jpg', img=frame)
                    webcam.release()
                    print("Processing image...")
                    img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                    print("Converting RGB image to grayscale...")
                    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                    print("Converted RGB image to grayscale...")
                    print("Resizing image to 28x28 scale...")
                    img_ = cv2.resize(gray, (28, 28))
                    print("Resized...")
                    img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                    print("Image saved!")

                    break
                elif key == ord('q'):

                    try:
                        check, frame = webcam.read()
                        print(check)  # prints true as long as the webcam is running
                        print(frame)  # prints matrix values of each framecd
                        cv2.imshow("Capturing", frame)
                        key = cv2.waitKey(1)
                        if key == ord('s'):
                            cv2.imwrite(filename='saved_img.jpg', img=frame)
                            webcam.release()
                            print("Processing image...")
                            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                            print("Converting RGB image to grayscale...")
                            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                            print("Converted RGB image to grayscale...")
                            print("Resizing image to 28x28 scale...")
                            img_ = cv2.resize(gray, (28, 28))
                            print("Resized...")
                            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                            print("Image saved!")

                            break

                        elif key == ord('q'):
                            webcam.release()
                            cv2.destroyAllWindows()
                            break

                    except(KeyboardInterrupt):
                        print("Turning off camera.")
                        webcam.release()
                        print("Camera off.")
                        print("Program ended.")
                        cv2.destroyAllWindows()
                        break

        elif "open mobile webcam" in query:
            speak("opening")
            url = "http://192.168.105.126:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(2)
                if q == ord("q"):
                    break;

            cv2.destroyAllWindows()