import os


class Config:

    API_ID = int(os.environ.get("API_ID",1543212))
    API_HASH = os.environ.get("API_HASH","d47de4b25ddf79a08127b433de32dc84")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","1780099168:AAHlhBygBSWnP39Ok8ycUqeNPjcP635SH4Y")
    SESSION_NAME = os.environ.get("SESSION_NAME", "TheScs_Robot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001376476949"))
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://david12345:david12345@cluster0.gstzk.mongodb.net/david12345?retryWrites=true&w=majority")
    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "1478357602").split(" ")]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 5))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
