import sys
import time
import random
import datetime
import telepot
import pyttsx3

def handle(msg):
	chat_id = msg['chat']['id']
	message = msg['text'] #we want to store both the message and the sender's ID
	print(chat_id, 'wrote:') 
	print('"',message,'"')
  #showing the message in the form of 
  #'UserID wrote:
  #"THIS IS THE MESSAGE"
  #if (chat_id == 0000000000) #uncomment this if you want to limit the users that can reproduce text, just put your ID instead of 0000000000
	engine = pyttsx3.init()
	rate = engine.getProperty('rate') #by default this value is too high to understand what it says, so i'm going to change it
	engine.setProperty('rate', rate-50) #if you want to speed up the voice, change the number 50 with some other number
	voice_id = 'italian' #delete this for english, change 'italian' to match your language
	engine.setProperty('voice', voice_id)
	engine.say(message)
	engine.runAndWait()
    
bot = telepot.Bot('XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') #insert your generated token here
bot.message_loop(handle)
print('Waiting for input...')

while 1:
	time.sleep(10)

