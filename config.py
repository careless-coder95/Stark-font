import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 31773201))
    API_HASH = os.environ.get("API_HASH", "4de8b7e5dec61796c782bdc400759248")
    OWNER_ID = int(os.environ.get("OWNER_ID", "8780379590"))  # Replace 123456789 with your actual numeric Telegram ID
