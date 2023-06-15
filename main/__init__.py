#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID"16995961, default=None, cast=int)
API_HASH = config("API_HASH"8817a7d4293049593e60999359970ddd , default=None)
BOT_TOKEN = config("BOT_TOKEN"6217840102:AAGXJ0yMrPT_edRmUkSVWJFEA3e3LikZVCw, default=None)
SESSION = config("SESSION"BQCmluXZkyv6Bjl6eCA6gX0Xex7XX1rhhxcd2gYt1Xc7DHXg4ccGUFqKMLgDo_be93jWymr8EP1uIvwpCunkkT1fEkiHY0ig4UEf-N8HfCQQqpgYr6fOMKkojTy2C8vYfJBLnSbJ4Vp25b7bMyapS0jK_oto1PPsVIAk-eCi6OhHYWGJo2jQ205UkJhpInBlBokvmzxcP07v8WtAhgQMyNci9XX5esIR8NVBzhfzfQFX4CLauC9ndKWccyS6ILhhyzJEJkTX7McW0XdMgXVl9R1oLoLmpTnxI4zEmCbt6eXJjzSSCiCbn7yibaAhRbCuHvfq3uxhxHoDLyops76syJbEYcxeBwA, default=None)
FORCESUB = config("FORCESUB"t.me/+2Hg_3iFLjkVmYmFl ,default=None) 

AUTH = config("AUTH", default=None, cast=int)

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
