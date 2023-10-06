from asyncio import exceptions
from calendar import calendar
from email.mime import audio
from http import server
from random import random
import random
from re import T
from tkinter.filedialog import asksaveasfilename
from urllib import response
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import *
from PIL import ImageTk,Image
import time
from time import ctime
import pyjokes
import pyautogui
import pywhatkit
import wolframalpha








engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)
# print(voices[0].id)

def speak(audio):

    engine.say(audio) 

    engine.runAndWait()



def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning Shiv")

    elif hour>11 and hour<18:
        speak("Good Afternoon Shiv")

    else:
        speak("Good Evening Shiv")

    speak("I am your assistance how may I help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshoald = 1
        r.energy_threshold=10000
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please......")

        

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivrajyelave2002@gmail.com', 'cknkquzmhaftyeij')
    server.sendmail('shivrajyelave2002@gmail.com',to,content)
    server.close()


def tellday():
    day =datetime.date.today()
    speak(calendar.day_name[day.weekday()])

def telltime():

    current_time = datetime.datetime.now().strftime('%I:%M %P')
    return current_time

def takescreenshot():
    myscreenshot= pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+"_screenshot.png")

try:
    app= wolframalpha.Client("WE75AY-TW24PA4QYA")
except Exception:
    print("Check your internet cnnection")





class Widget:
    def __init__(self):
        root = Tk()

        root.title('Shiv')
# root.geometry('520×320')

        img = ImageTk.PhotoImage(Image.open('lena1.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right',fill='both',expand='no')

        compText = StringVar()


        userText = StringVar()
        userText.set('your Virtual Assistance')
        userFrame =LabelFrame(root,text='Shiv',font=('Railways',24,'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame,textvariable=userText, bg='black',fg='white')
        top.config(font=("Century Gothic", 15,'bold'))
        top.pack(side='top', fill='both', expand='yes')


        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')


        wishme()
        root.mainloop()
        
        

    def clicked(self):
        
        query=takeCommand().lower()
        speak(audio)
        if 'wikipedia' in query:
            speak('Searching on Wikidedia.....')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        

                        #  <---------------------OPEN---------------->

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

 

        elif 'open code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'open antivirus' in query:
            codePath = "C:\Program Files\Common Files\McAfee\Platform\McUICnt.exe"
            os.startfile(codePath)


                               #  <--------------------- MAIL---------------->


        elif 'mail to shiv' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "shivyelave@gmail.com"
                sendEmail(to,content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send email")

        elif 'mail to aishwariya' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "aretawade20ite@student.mes.ac.in"
                sendEmail(to,content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send email")

        elif 'mail to rutika' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "srutika20ite@student.mes.ac.in"
                sendEmail(to,content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send email")

        elif 'mail to anutej' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "aware20ite@student.mes.ac.in"
                sendEmail(to,content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send email")

        elif 'mail to jeevan' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "jkalbhor20ite@student.mes.ac.in"
                sendEmail(to,content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send email")

        elif 'mail to umesh' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "yelaveumesh0@gmail.com"
                sendEmail(to,content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send email")



        # elif 'about today' in query:
        #     speak('Sir today is '+ ctime())
        #     print('Sir today is '+ ctime())

        # elif 'the time' in query:
        #     current_time =telltime()
            
        
        # elif 'today is ' in query:
        #     tellday()

        elif 'are you' in query:
            speak('I am Gulabjam made by shiv')

        elif 'exit' in query:
            speak("Thank you sir, Have a nice day ")
            exit()

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
        
        elif 'take screenshot' in query:

            speak("sir, please select path")        
            takescreenshot()


        elif 'play' in query:
            speak('playing'+ query)
            pywhatkit.playonyt(query)

        elif 'about yourself' in query:
            speak('I am gulabjam. made for shiv')


        elif 'temperature' in query:
            try:
                res= app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except Exception:
                print("please, Check your internet cnnection")
                speak("please, Check your internet cnnection")


        elif 'time' in query:
            try:
                res= app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except Exception:
                print("please, Check your internet cnnection")
                speak("please, Check your internet cnnection")

        elif 'plus' in query:
            try:
                res= app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except Exception:
                print("please, Check your internet cnnection")
                speak("please, Check your internet cnnection")


        elif 'multiplied by' in query:
            try:
                res= app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except Exception:
                print("please, Check your internet cnnection")
                speak("please, Check your internet cnnection")


        # elif 'game' in query:
            
        #     speak("chose among rock, paper, scissor")
        #     pmove=takeCommand()
        #     moves=["rock", "paper", "scissor"]
        #     cmove=random.choice(moves)
            

        #     speak("The computer chose "+cmove)
        #     speak("and you chose "+pmove)
        #     print("The computer chose "+cmove)
        #     print("You chose "+pmove)

        #     if pmove==cmove:
        #         speak("The match is draw")
        #         print("The match is draw")
        #     elif pmove=='rock' and cmove=='scissor':
        #         speak("Player wins")
        #         print("Player wins")
            
        #     elif pmove=='rock' and cmove=='paper':
        #         speak("computer wins")
        #         print("computer wins")
            
        #     elif pmove=='rock' and cmove=='scissor':
        #         speak("Player wins")
        #         print("Player wins")
            
        #     elif pmove=='paper' and cmove=='scissor':
        #         speak("computer wins")
        #         print("computer wins")
            
        #     elif pmove=='paper' and cmove=='rock':
        #         speak("player wins")
        #         print("player wins")
            
        #     elif pmove=='scissor' and cmove=='paper':
        #         speak("Player wins")
        #         print("Player wins")

        #     elif pmove=='scissor' and cmove=='rock':
        #         speak("computer wins")
        #         print("computer wins")
            

        # elif 'toss a coin' in query:
        #     moves["head", "tails"]
        #     cmove=random.choice(moves)
        #     print('Its '+cmove)
        #     speak('Its '+cmove)




if __name__=="__main__":

    widget=Widget()
    while True:
        query=takeCommand()
    
    


