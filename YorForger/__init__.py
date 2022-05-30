

import logging
import os
import sys
import time

import spamwatch
import telegram.ext as tg
from pyrogram import Client, errors
from redis import StrictRedis
from telethon import TelegramClient
from telethon.sessions import MemorySession
# from YorForger import config

StartTime = time.time()

# enable logging
FORMAT = "[YorForger] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger(__name__)

LOGGER.info("[Yor] Starting Yor...")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "[Yor] You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("[Yor] Your OWNER_ID env variable is not a valid integer.")

    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}
    except ValueError:
        raise Exception(
            "[Yor] Your dev users list does not contain valid integers."
        )

    try:
        SUPPORT_USERS = {int(x) for x in os.environ.get("SUPPORT_USERS", "").split()}
    except ValueError:
        raise Exception(
            "[Yor] Your support users list does not contain valid integers."
        )

    try:
        WHITELIST_USERS = {
            int(x) for x in os.environ.get("WHITELIST_USERS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Yor] Your whitelisted users list does not contain valid integers."
        )
    try:
        DEMONS = {
            int(x) for x in os.environ.get("DEMONS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Yor] Your demon users list does not contain valid integers."
        )

    try:
        WHITELIST_CHATS = {
            int(x) for x in os.environ.get("WHITELIST_CHATS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Yor] Your whitelisted chats list does not contain valid integers."
        )
    try:
        BLACKLIST_CHATS = {
            int(x) for x in os.environ.get("BLACKLIST_CHATS", "").split()
        }
    except ValueError:
        raise Exception(
            "[Yor] Your blacklisted chats list does not contain valid integers."
        )

    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    DB_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    REDIS_URL = os.environ.get("REDIS_URL")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    DONATION_LINK = os.environ.get("DONATION_LINK")
    LOAD = os.environ.get("LOAD", "").split()
    TEMP_DOWNLOAD_DIRECTORY = ("./")
    NO_LOAD = os.environ.get("NO_LOAD", "").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
 
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CUSTOM_CMD = os.environ.get("CUSTOM_CMD", False)
    API_WEATHER = os.environ.get("API_OPENWEATHER", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    SPAMWATCH = os.environ.get("SPAMWATCH_API", None)
    SPAMMERS = os.environ.get("SPAMMERS", None)

else:
    from YorForger.config import Development as config

    TOKEN = config.TOKEN
    try:
        OWNER_ID = int(config.OWNER_ID)
    except ValueError:
        raise Exception("[Yor] Your OWNER_ID variable is not a valid integer.")

    MESSAGE_DUMP = config.MESSAGE_DUMP
    OWNER_USERNAME = config.OWNER_USERNAME

    try:
        DEV_USERS = {int(x) for x in config.DEV_USERS or []}
    except ValueError:
        raise Exception(
            "[Yor] Your dev users list does not contain valid integers."
        )

    try:
        SUPPORT_USERS = {int(x) for x in config.SUPPORT_USERS or []}
    except ValueError:
        raise Exception(
            "[Yor] Your support users list does not contain valid integers."
        )

    try:
        WHITELIST_USERS = {int(x) for x in config.WHITELIST_USERS or []}
    except ValueError:
        raise Exception(
            "[Yor] Your whitelisted users list does not contain valid integers."
        )
    try:
        DEMONS = {int(x) for x in config.DEMONS or []}
    except ValueError:
        raise Exception(
            "[Yor] Your demons list does not contain valid integers."
        )
    try:
        WHITELIST_CHATS = {int(x) for x in config.WHITELIST_CHATS or []}
    except ValueError:
        raise Exception(
            "[Yor] Your whitelisted chats list does not contain valid integers."
        )
    try:
        BLACKLIST_CHATS = {int(x) for x in config.BLACKLIST_CHATS or []}
    except ValueError:
        raise Exception(
            "[Yor] Your blacklisted users list does not contain valid integers."
        )

    WEBHOOK = config.WEBHOOK
    URL = config.URL
    PORT = config.PORT
    CERT_PATH = config.CERT_PATH

    DB_URI = config.SQLALCHEMY_DATABASE_URI
    REDIS_URL = config.REDIS_URL
    DONATION_LINK = config.DONATION_LINK
    LOAD = config.LOAD
    NO_LOAD = config.NO_LOAD
    DEL_CMDS = config.DEL_CMDS
    STRICT_GBAN = config.STRICT_GBAN
    WORKERS = config.WORKERS
    BAN_STICKER = config.BAN_STICKER
    ALLOW_EXCL = config.ALLOW_EXCL
    CUSTOM_CMD = config.CUSTOM_CMD
    API_WEATHER = config.API_OPENWEATHER
    WALL_API = config.WALL_API
    SUPPORT_CHAT = config.SUPPORT_CHAT
    API_HASH = config.API_HASH
    API_ID = config.API_ID
    SPAMWATCH = config.SPAMWATCH_API
    SPAMMERS = config.SPAMMERS

# Dont Remove This!!!
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(949365920)
BOT_ID = 5118086248

# Pass if SpamWatch token not set.
if SPAMWATCH is None:
    spamwtc = None
    LOGGER.warning("[Yor] Invalid spamwatch api")
else:
    spamwtc = spamwatch.Client(SPAMWATCH)

REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)
try:
    REDIS.ping()
    LOGGER.info("[Yor] Your redis server is now alive!")
except BaseException:
    raise Exception("[Yor] Your redis server is not alive, please check again.")
finally:
    REDIS.ping()
    LOGGER.info("[Yor] Your redis server is now alive!")

# Telethon
client = TelegramClient(MemorySession(), API_ID, API_HASH)
updater = tg.Updater(
    TOKEN,
    workers=min(32, os.cpu_count() + 4),
    request_kwargs={"read_timeout": 10, "connect_timeout": 10},
)
dispatcher = updater.dispatcher

pbot = Client("ErenPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
pbot.start()
telethn = TelegramClient("luna", API_ID, API_HASH)


DEV_USERS = list(DEV_USERS)
WHITELIST_USERS = list(WHITELIST_USERS)
SUPPORT_USERS = list(SUPPORT_USERS)
DEMONS = list(DEMONS)

# Load at end to ensure all prev variables have been set
# pylint: disable=C0413
from YorForger.modules.helper_funcs.handlers import CustomCommandHandler

if CUSTOM_CMD and len(CUSTOM_CMD) >= 1:
    tg.CommandHandler = CustomCommandHandler


def spamfilters(text, user_id, chat_id):
    # print("{} | {} | {}".format(text, user_id, chat_id))
    if int(user_id) not in SPAMMERS:
        return False

    print("[Yor] This user is a spammer!")
    return True
    
if DEV_USERS != 949365920:
    LOGGER.warning("DEV_USERS must have id '949365920'")
else:
    DEV_USERS = list(DEV_USERS)