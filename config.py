import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "25465082")
API_HASH = os.getenv("API_HASH", "4a6b5e40c8bc08c8af09add6cca23b18")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7598927328:AAG0ncbt20aSKSxFnVtnDJiRZ5zZwTsO4Qk")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://username:password@cluster0.xe5grh2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "7388366658").split()))
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None)
LOG_GROUP = int(os.getenv("LOG_GROUP", "0"))
FORCE_SUB = int(os.getenv("FORCE_SUB", "0"))
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F")
YT_COOKIES = os.getenv("YT_COOKIES", "")
INSTA_COOKIES = os.getenv("INSTA_COOKIES", "")
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "1000"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/IMAXBots")
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/ORGSupports")
