#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID",16995961)
API_HASH = config("API_HASH",8817a7d4293049593e60999359970ddd)
BOT_TOKEN = config("BOT_TOKEN",6281366465:AAFqBusQtunH7ZXjtHQ9bjlQOYvnhwQXqcs)
SESSION = config("SESSION", BQEDVnkAg-mGo-LinOgVbquy8-YJigv-ve9gSHrBGF2ud_peCE3UCBcnp-gcQrUdbqmxmAgDioZ2cb_UAv3jjJqLCdF8tg2hK1yz0DsSQmqG6ep-9BpUoLi4WI5y2DKd-AW5hM6jsk8iC2B3_oVGWLxxw1O7wwl6ulgWvoDDoQawCfyZdox0sS8jY9pTrKRACHYAxz4wXQ_GIwA0FDtuCuwlbF3pfQ7yo2nZT4CL7d9xbOwv1N8D7chz1nMx9Qu2M5ObZJi4aHFsrtSoCbebhzzifXracr3eobm9n13QmGuPNkpMqgFekwqwKdL-cyM44p9uXEByfqspkZAnEEuDvEsjDM0xLQAAAABhzF4HAA)
FORCESUB = config("FORCESUB",nothingboy593)
AUTH = config("AUTH",1640783367)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
