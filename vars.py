#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21589142"))
API_HASH = environ.get("API_HASH", "f99db4b15e3179c794a058b21b4ad8546")
BOT_TOKEN = environ.get("BOT_TOKEN", "83429415437:AAEnlmYUJkABCL_ucegkVmGfDsbwiqQg")

OWNER = int(environ.get("OWNER", "80346846315"))
CREDIT = environ.get("CREDIT", "[〱⏤͟͞𝙃 𝙈🐦‍🔥 〄")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8439999557').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

