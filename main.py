import pyttsx3                          #pip install pyttsx3
import datetime
import speech_recognition as sr         #pip install SpeechRecognition
import wikipedia                        #pip install wikipedia
import smtplib, ssl                     #smtp server
import os, sys, subprocess
from dotenv import load_dotenv
import webbrowser as wb                 #web browser
import psutil                           #pip install psutil
#import pyjokes                          #pip install pyjokes
import pyautogui                        #pip install pyautogui, screenshot
import re
import random
#import wolframalpha                    #calculator  #pip install wolframalpha 
import json
import requests
from urllib.request import urlopen
import time

engine = pyttsx3.init()
#wolframalpha_app_id='wolfram alpha id here'

#engine.setProperty('voice', voices[1].id)  # this is female voice

# ##LIST OF VOICES
# voices = engine.getProperty('voices')
# for v in voices:
#     #print(v.id)
#     if v.id=="english":
#         print(v)
#     #if v.gender=="female":
#     #    print(v)

##DOTNET INFORMATION
load_dotenv()
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")
####################



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def this_time():
    thisTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is: "+thisTime)
    print ("the current time is: "+thisTime)

def this_date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    #speak("the current day is: "+str(day)+" the month "+str(month)+" and the year is "+str(year))
    #print("the current day is: "+str(day)+" the month "+str(month)+" and the year is "+str(year))

    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

def Greetings():
    this_date()
    speak("How can I help you?")

def Listening():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1
        #speak("I'm llistining")
        audio=r.listen(source)
    
    try:
        print("Recognizing.......")
        query=r.recognize_google(audio,language='en-US')
        #query=r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        print("Say thath again please.......")
        return "None"
    return query

def sendEmail(reciever,content):
    context=ssl.create_default_context()
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    #server.starttls()
    server.login(EMAIL,PASSWORD)
    server.sendmail(EMAIL,reciever,content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    print("the CPU is at "+usage)
    battery=psutil.sensors_battery()
    print("the battery percent is ")
    print(battery.percent)

'''
def jokes():
    print(pyjokes.get_joke())
'''
def screenshot():
    scr=pyautogui.screenshot()
    #scr.save('/home/kira/Downloads/img.png')        ##Doesn't work 

##WELCOME
welcome="hello dennys, how are doing ?"


if __name__ == "__main__":
##for now    Greetings()
    #print("this show the begining")
    while True:
        #query=Listening().lower() #all words will be stored in lower case for easy recognition
        query='where is new york'
        if 'time' in query:
            this_time()

        elif 'date' in query:
            this_date()

        #wikipedia search
        elif 'wikipedia' in query:
            speak("Searching....")
            print("Searching....")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)

        #smtp server
        elif 'email' in query:
            try:
                content=query.replace('email','')
                print('This is content: '+content)
                speak("who is the receiver?")
                print("who is the receiver?")
                reciever=input("Please enter the email of the receiver: ")
                #content="hello test number 3"
                sendEmail(reciever, content)
                print("The Email has been sent.")
            
            except Exception as e:
                print(e)
                print("Unable to send the email")

        elif 'open webpage' in query:
            speak("what do you want to search in the browser?")
            print("what do you want to search in the browser?")
            chromepath='/usr/bin/google-chrome-stable %s'          #the path of the driver of google chrome
            #search=Listening().lower()
            search=input('enter the webpage: ')
            wb.get(chromepath).open_new_tab(search+'.com')
            wb.get(chromepath).open_new_tab(search+'.org')

        elif 'search in google' in query:
            speak("what do you want to search in google?")
            print("what do you want to search in google?")
            #search=Listening().lower()
            search=input('enter the what do you want to search in google: ')
            wb.open('https://www.google.com/search?q='+search)

        elif 'search in youtube' in query:
            speak("what do you want to search in youtube?")
            print("what do you want to search in youtube?")
            #search=Listening().lower()
            search=input('enter the what do you want to search in youtube: ')
            wb.open('https://www.youtube.com/results?search_query='+search)

        elif 'cpu' in query:
            cpu()

        #elif 'jokes' in query:
        #    jokes()
        
        elif 'quit' in query:
            speak('Going Offline Sir!')
            print('Going Offline Sir!')
            quit()

        # elif 'app' in query:
        #     print('Opening the App....')
        #     app=r'/usr/bin/google-chrome-stable'
        #     #os.startfile(app)
        #     os.system('xdg-open '+app)

        elif 'write a note' in query:
            speak('What should I write? Sir!')
            print('What should I write? Sir!')
            content=Listening()
            note=open('note.txt','w')
            speak('Sir should I include Date and Time?')
            answer=Listening()
            if 'yes' in answer or 'sure' in answer:
                time= this_time()
                note.write(time)
                note.write(':-')
                note.write(content)
                speak('Done Sir!')
                print('Done Sir!')
            else:
                note.write(content)
                speak('Done Sir!')
                print('Done Sir!')

        elif 'show notes' in query:
            #speak('Showing notes Sir!')
            print('Showing notes Sir!')
            note=open('dennys.txt','r')
            #speak(note.read())
            print(note.read())
            quit()

        elif 'screenshot' in query:
            screenshot()
            quit()
        
        elif 'play music' in query:
            music_dir="/home/kira/projects/downloader/"
            music=os.listdir(music_dir)
            #speak('What should I play')
            print('What should I play')
            #answer=Listening().lower()
            answer="Fighters"
            query2=answer.lower()
            music_lw = [x.lower() for x in music] #lowercase a list

            print(music)
            print(music_lw)
            print("-------")
            # if query2 in music_lw:
            #     print("music exist")
            # else:
            #     print("sorry Sir, that music doesn't exist")
            
            # print("-------")
            for a in music:
                if a.endswith(".mp3"):
                    print(a)
            
            #development by dennys
            '''
            for a in music:
                print(a)
                print(a.lower())
                b=a.lower()
                print("-------")
                if query2 in b:
                    print ("checked")
                    print("the song exists")
                    #speak("the song exists")
                    if sys.platform == "win32":
                        os.startfile(music_dir+a)
                        print("this is playing: "+a)
                        speak("this is playing: "+b)
                        print("-------")
                    else:
                        opener = "open" if sys.platform == "darwin" else "xdg-open"
                        #subprocess.call([opener, music_dir+a])
                        print(music_dir+"'"+a+"'")
                        print("this is playing: "+a)
                        #speak("this is playing: "+b)
                        print("-------")
                else:
                    print("not checked")
                    print("-------")
                '''
            ## udemy    
            # while('number' not in ans and ans != 'random' and ans != 'you choose'):
            #     print("I could not understand you. Please try again")
            #     ans= Listening().lower()
            
            # if 'number' in ans:
            #     no=int(ans.replace('number',''))
            # elif 'random' or 'your choose' in ans:
            #     no=random.randint(1,100)
            #os.startfile(os.path.join(songs_dir,music[no]))


            quit()
        
        elif 'where is' in query:
            query=query.replace("where is", "")
            location=query
            print("Sir, you asked to locate "+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
            quit()

        elif 'news' in query:
            try:
                #jsonObj=urlopen("https://newsapi.org/v2/everything?q=tesla&from=2022-03-27&sortBy=publishedAt&apiKey=0302968baeae4926899b36a4ad8f7d1a")
                #jsonObj=urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0302968baeae4926899b36a4ad8f7d1a")
                jsonObj=urlopen("https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=0302968baeae4926899b36a4ad8f7d1a")
                data=json.load(jsonObj)
                i=1

                print("Here are some top headlines from the Entertainment Industry")
                print("-----TOP HEADLINES-----"+"\n")
                for a in data['articles']:
                    print(str(i)+'- '+a['title']+'\n')
                    print(a['description']+'\n')
                    #speak(a['title'])
                    i+=1
                quit()
            
            except Exception as e:
                print(str(e))

        
        # elif 'calculate' in query:
        #     client=wolframalpha.Client(wolframalpha_app_id)
        #     a=query.lower().split().index('calculate')
        #     query=query.split()[a + 1:]
        #     ans=client.query(''.join(query))
        #     answer=next(ans.results).text
        #     print("The answer is "+answer)
        #     quit()

        # elif 'what is' in query or'who is' in query:
        #     client=wolframalpha.Client(wolframalpha_app_id)
        #     a=client.query(query)
        #     try:
        #         print(next(a.results).text)
        #     except StopIteration:
        #         print("No results")
        #     quit()
        

        elif 'stop listening' in query:
            print("How many seconds do you want to finish the listening")
            ans=int(Listening())
            time.sleep(ans)
            print(ans+" seconds for stop virtual assistant")
            quit()


        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
  