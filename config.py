# yooo guiz Herox 
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "TrickyAbhi-Music")
API_ID = int(getenv("API_ID", "8945070"))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "Herox_xd")
ALIVE_NAME = getenv("ALIVE_NAME", "TrickyAbhi-Music")
BOT_USERNAME = getenv("BOT_USERNAME", "TrickyAbhi_Music_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TrickyAbhi_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TrickyAbhii_Op")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Techno_Trickop")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5124507794").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2374f6ac4dd79c2ed9639.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SJMxADITI/HellMusic")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/596f75a52ea9bf0109644.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")

