from aiogram.dispatcher import Dispatcher
from aiogram import Bot
import os

TOKEN = os.getenv('5466053732:AAHZJK3wOusCldo3xTNAkevzEKAVGVqcqXM')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('desolate-caverns-75711')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
DB_URL = os.getenv('DATABASE_URL')
