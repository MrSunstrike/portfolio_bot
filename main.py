import sys
from os import getenv

from dotenv import load_dotenv
from telegram.ext import Application

from handlers import (choose_photo_handler, get_back_handler,
                      send_docs_handler, send_essay_handler,
                      send_photo_handler, start_handler, voice_message_handler)
from logger import setup_logger

# инициируем логгер
logger = setup_logger("main")

# достаем токен из окружения
load_dotenv()
BOT_TOKEN = getenv('BOT_TOKEN')

# инициируем бота под нашим токеном
try:
    application = Application.builder().token(BOT_TOKEN).build()
except Exception as e:
    logger.critical(f'Доступ к токену не был получен: {e}')
    sys.exit()


# регистрируем все ручки
application.add_handler(start_handler)
application.add_handler(send_docs_handler)
application.add_handler(choose_photo_handler)
application.add_handler(get_back_handler)
application.add_handler(send_photo_handler)
application.add_handler(voice_message_handler)
application.add_handler(send_essay_handler)


# слушаем сообщения пользователей
application.run_polling()
