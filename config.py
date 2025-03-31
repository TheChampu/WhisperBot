from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 29893020))
API_HASH = getenv("API_HASH", "28e79037f0b334ef0503466c53f08af5")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 7006524418))
SUPPORT_GRP = "ShivanshuHUB"
UPDATE_CHNL = "akaChampu"
OWNER_USERNAME = "itsMeShivanshu"
    