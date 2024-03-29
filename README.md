# TelegramVoice2Pi
A bot to play telegram messages as audio
## WHAT DOES IT DO?
This is a simple program that uses Telegram Bot API to receive text messages from one or more users and play them as audio. I made this to be run on a headless RPi that is going to be set-up in my living room, connected via AUX to a speaker, and it will be used to stream ~~not so~~ useful messages to my flatmates
## REQUIREMENTS:
- Telegram with @BotFather (just start a conversation with it, generate a new bot and write down the token which is in the form of `XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)
- Python 3 with pip
- Git
- Libespeak1 and Espeak (to play voice from the speaker)
- Suggested use of venv (it might cause conflicts with pip packages)
```
sudo apt install python3.8 python3-pip git libespeak1 espeak
```
- PYTTSX3 and TELEPOT
```
pip3 install pyttsx3 telepot
```
Once you have met the requirements above, just type the following:
```
git clone https://github.com/Whoneon/TelegramVoice2Pi.git
cd TelegramVoice2Pi
nano Bot.py
```
Now you have to change the string `XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` and paste there your token (generated above), then save with `CTRL + O`
## RUN IT!
Just type
```
python3 Bot.py
```
Now leave the command window running: this will keep the bot on listen mode. Try to type something in the bot chat (during the set-up phase, it will ask you to choose a @nickname, just start a conversation with that)
## ADJUSTMENT(S)
If you open the code, you will see some useful comments. If you wish to change the language or the speed of voice, just follow the instructions!
