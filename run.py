import time
import pyautogui, threading
from python_imagesearch.imagesearch import imagesearch 

import speech_recognition as sr
import pyaudio





#you can multiple or rome the codos below.  
#first 
def first():
    while True:
        first= imagesearch('./image1.png')
        
        if first != [-1,-1]:

            print('found it')
            pyautogui.leftClick(first[0],first[1])
            time.sleep(18)
            
        
    
        
        else:
            print('I am sorry, we couldnt find it.')

    

thread1= threading.Thread(target=first)
thread1.start()

#second
def second():
    while True:
        second= imagesearch('./image2.png')
        if second  != [-1,-1]:
            print('found second')
            pyautogui.leftClick(second[0],second[1])
        
            time.sleep(10)
        else:
            print('couldnt find second')

thread2=threading.Thread(target=second)
thread2.start()

#third
def third():
    while True:
        
        third= imagesearch('./image3.png')

        if third  != [-1,-1]:
            print('found ittt')
            pyautogui.leftClick(third[0],third[1])
        
            time.sleep(10)
        else:
            print('we didint find third')

thread3=threading.Thread(target=third)
thread3.start()

#fourth
def fourth():
    while True:
        fourth= imagesearch('./image4.png')
        if fourth  != [-1,-1]:
            print('found fourth')
            pyautogui.leftClick(fourth[0],fourth[1])
        
            time.sleep(10)
        else: 
            print('we didint find fourth')

thread4=threading.Thread(target=fourth)
thread4.start()

#fifth
def fifth():
    
    while True:
        fifth= imagesearch('./image6.png')
        ok= imagesearch('./ok.png') # if you want to click an image when another image comes along.  
        if ok  != [-1,-1]:
            print('found fifth')
            pyautogui.leftClick(fifth[0],fifth[1])
        
            time.sleep(10)
        else: 
            print('we didint find fifth')

thread5=threading.Thread(target=fifth)
thread5.start()

#sixth
def sixth():
    while True:
        sixth= imagesearch('./image7.png')
        if sixth  != [-1,-1]:
            print('found sound')
            pyautogui.leftClick(sixth[0],sixth[1])
        
            time.sleep(10)
        else: 
            print('we didint find sixth')
thread6=threading.Thread(target=sixth)
thread6.start()

#seventh
#You can also use those codes for should have been clicked when sounds came. 
def seventh():
    while True:
        time.sleep(3)
        play= imagesearch('./replay.png')
        r = sr.Recognizer()
        mm=[540,49]
        
        

        if play != [-1,-1]:
    
            time.sleep(3)
            print('it works.')
            pyautogui.leftClick(play[0],play[1])
            time.sleep(4)
            with sr.Microphone() as source:                # use the default microphone as the audio source
                audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
            try:
                text = r.recognize_google(audio, language='en-US', show_all=True) #set up language as you want exaple en-UK 
                    
                print (text)
                
                
                #pyautogui.leftClick(mm[0],mm[1]) #.actions.send_keys(text.lower())
                    #actions.perform()
                                
                # recognize speech using Google Speech Recognition
            except LookupError:                            # speech is unintelligible
                print("Could not understand audio")
        
        else:
            print('doesnt work')

thread7=threading.Thread(target=seventh)
thread7.start()
