#https://github.com/Whoneon/TelegramVoice2Pi
#feel free to use, improve or edit my code! 
# - Whoneon

import sys
import time
from datetime import datetime
import telepot
import pyttsx3

def handle(msg):
        chat_id = "@" + msg['chat'].setdefault('username',"") + " (" + msg['chat'].setdefault('first_name',"") + msg['chat'].setdefault('last_name',"") + ")"
        user_id = " (id = " + str(msg['chat']['id']) + ")"
        message = msg['text']
        ct = datetime.now()
        content = "-{0} : {1}{3} wrote: {2}"
        print(content.format(ct.strftime("%Y-%m-%d %H:%M:%S"), chat_id, message,"")) #Console printing just the timestamp, username and message that is being read
        print(content.format(ct.strftime("%Y-%m-%d %H:%M:%S"), chat_id, message, user_id), file=open('log.txt', 'a')) #verbose output stored in a log file (might be useful to store both the ID and the username in case someone changes their Telegram @)
	
	#if (user_id == 0000000000): #uncomment this if you want to limit the users that can reproduce text, just put your telegram ID instead of 0000000000
	engine = pyttsx3.init()
        rate = engine.getProperty('rate') #by default this value is too high to understand what it says, so i'm going to change it
        engine.setProperty('rate', rate-50) #if you want to speed up the voice, change the number 50 with some other number
        voice_id = 'italian' #delete this for english, change 'italian' to match your language
        engine.setProperty('voice', voice_id)
	engine.say(message)
	engine.runAndWait()

bot = telepot.Bot('XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') #insert your generated token here (via BotFather on Telegram)
bot.message_loop(handle)
print('Waiting for input...')

while 1:
	time.sleep(10)
