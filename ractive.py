import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import numpy as np 
import pandas as pd 
from win32com.client import Dispatch
import pywhatkit as kit


df1 = pd.read_excel("D:/visual studio code/visual codes/friend phone number.xlsx")
final_contacts = dict(zip(list(df1['name']),list(df1['ph number'])))
# print(final_contacts)
def speak(text):
    speak = Dispatch('SAPI.SpVoice')
    speak.speak(text)

passcode = "nirbhay"    

def recognise(n):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text  = r.record(source,duration=n)
        try:
            recognised = r.recognize_google(text)
            return recognised
        except:
            return None
def work():
    speak("tell me what can i do for you")
    while True:
        a = recognise(4)
        if a!=None:
            print(a)
            if "send" in a and "message" in a:
                p = a.split()[-1].lower()
                if p in set(final_contacts.keys()):
                    speak("please tell the message")
                    msg = recognise(10)
                    speak(f"the message is {msg} should i send it")
                    finalcall = recognise(4)
                    if 'no' in finalcall.lower():
                        speak('ok you may try once again')
                    else:
                        webbrowser.open('https://www.google.com/')
                        kit.sendwhatmsg(final_contacts[p],msg,datetime.datetime.now().hour,datetime.datetime.now().minute+1,wait_time=10) 
                else:
                    speak(f"the name {p} is not in your list")
            elif 'search' in a.lower():
                speak("what do you want to search")
                thesearch = recognise(10)
                speak('where to search sir google/youtube')
                recognisekarlo = recognise(3)
                if 'google' in recognisekarlo.lower():
                    webbrowser.open("https://www.google.com/?#q="+ thesearch)
                if 'youtube' in recognisekarlo.lower():
                    webbrowser.open('https://www.youtube.com/results?search_query='+ thesearch)

            elif 'google' in a.lower() and 'meet' not in a.lower() and 'kill' not in a.lower() and 'close' not in a.lower() and 'stop' not in a.lower():
                speak("opening google")
                webbrowser.open("https://www.google.com/")
            elif 'youtube' in a.lower():
                speak('opening youtube..')
                webbrowser.open('https://www.youtube.com/')
            elif 'gmail' in a.lower() or 'mail' in a.lower():
                speak('opening gmail..')
                webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            elif 'wish me' in a.lower().strip() or 'wish us' in a.lower().strip():
                atp= datetime.datetime.now().hour
                if 0<= atp < 12:
                    speak('good morning nirbhay sir, have a nice day')
                elif 12<=atp<16:
                    speak('good afternoon nirbhay sir, have a nice day')
                elif 16<=atp<23:
                    speak('good evening nirbhay sir, have a nice day')
            elif 'are you there' in a.lower():
                speak("yes sir i am listening...")
            elif 'class' in a.lower() or 'meet' in a.lower():
                if 'electrical' in a.lower():
                    webbrowser.open("https://meet.google.com/lookup/bfozqwol6m?authuser=0&hs=179")
                elif '2021' in a.lower():
                    webbrowser.open("https://meet.google.com/lookup/hl5kwpehcu")
                elif "energy material" in a.lower():
                    webbrowser.open("https://meet.google.com/lookup/dnvx4qkedy")
                elif "quantum" in a.lower():
                    webbrowser.open("https://meet.google.com/lookup/hl5kwpehcu")
            elif 'music' in a.lower():
                choice = random.choice([1,2])
                if choice==1:
                    df = pd.read_excel("D:/visual studio code/visual codes/ractive_instructions.xlsx")
                    awful = list(df['youtube music link'])
                    webbrowser.open(random.choice(awful))
                else:
                    os.chdir('D:/New folder/MUSIC')
                    ab = os.listdir('D:/New folder/MUSIC')
                    os.startfile(random.choice(ab))
            elif 'hi' in a.lower() or 'hey' in a.lower() or 'hay' in a.lower() or 'hello' in a.lower() or 'how' in a.lower():
                speak("i am fine sir , how are you")
            elif 'tell me about yourself' in a:
                speak("i am ractive 2.0 , and i have been created by nirbhay sharma")
            elif 'what can you do' in a:
                speak("i can follow your instructions that are coded in me")
            elif 'friend list' in a or 'show my friends list' in a:
                with open('D:/visual studio code/visual codes/file1.txt','w') as f:
                    for i , j in final_contacts.items():
                        f.write(f"{i},{j}\n")
                os.startfile('D:/visual studio code/visual codes/file.txt')
            elif 'stop' in a.lower() or "close" in a.lower() or "kill" in a.lower():
                if 'notepad' in a.lower():
                    os.system('taskkill/im notepad.exe')
                if 'pycharm' in a.lower():
                    os.system('taskkill/im pycharm64.exe')
                if 'idea' in a.lower() or 'java' in a.lower():
                    os.system('taskkill/im idea64.exe')
                if 'vlc' in a.lower():
                    os.system('taskkill/im vlc.exe')
                if 'chrome' in a.lower() or 'google' in a.lower():
                    os.system('taskkill/im chrome.exe')
            elif 'time' in a.lower() or 'date' in a.lower():
                speak("the time is "+str(datetime.datetime.now().hour)+'hour'+str(datetime.datetime.now().minute)+"minute")
                l = {1:'january',2:'february',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
                speak('the date is '+str(datetime.date.today().day)+l[datetime.date.today().month]+str(datetime.date.today().year))
            elif 'what is your name' in a.lower():
                speak("my name is ractive and I am first artificial intelligence creted by you nirbhay sir")
            elif 'exit' in a.lower() or 'sleep' in a.lower() or 'leave' in a.lower():
                speak("as you wish , ractiv signing off")
                break



work()    


