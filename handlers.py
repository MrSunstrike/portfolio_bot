from text import TEXT_DICT as TEXT, STICKERS_DICT as STICKER
from keyboards import KEYBOARDS as KB
from keyboards import main_markup, photo_markup
from telegram.ext import MessageHandler, CommandHandler, filters
from telegram import InputMediaPhoto
import random
import os

async def start(update, context):
    '''Функция для приветственного хэндлера'''
    await context.bot.send_sticker(chat_id=update.effective_chat.id,
                                   sticker=STICKER['hi'])
    await update.message.reply_text(TEXT['hi1'])
    await update.message.reply_text(TEXT['hi2'])
    await update.message.reply_text(TEXT['hi3'], reply_markup=main_markup)

start_handler = CommandHandler('start', start)


async def choose_photo(update, context):
    '''Функция для хэндлера, уточняющего, какое фото требуется'''
    await update.message.reply_text(TEXT['photo'], reply_markup=photo_markup)
    
choose_photo_handler = MessageHandler(
    filters.Regex(f"^{KB['main'][0][0]}$"), choose_photo
)


async def get_docs(update, context):
    '''Функция для хэндлера, отправляющего доку'''
    await update.message.reply_text(TEXT['docs'], reply_markup=main_markup)

get_docs_handler = MessageHandler(
    filters.Regex(f"^{KB['main'][2][0]}$"), get_docs
)


async def get_back(update, context):
    '''Функция для хэндлера, возвращающего основную клавиатуру'''
    await update.message.reply_text(TEXT['back'], reply_markup=main_markup)

get_back_handler = MessageHandler(
    filters.Regex(f"^{KB['photo'][3][0]}$"), get_back
)

async def send_photo(update, context):
    if update.message.text == KB['photo'][0][0]:
        folder_path = "./media/img/school/"
    elif update.message.text == KB['photo'][1][0]:
        folder_path = "./media/img/selfie/"
    else:
        folder_path = "./media/img/work/"
    photos = os.listdir(folder_path)
    photo_path = os.path.join(folder_path, random.choice(photos))
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(photo_path, 'rb'))

send_photo_handler = MessageHandler(
    filters.Regex(
        f"^({KB['photo'][0][0]}|{KB['photo'][1][0]}|{KB['photo'][2][0]})$"
    ), send_photo
)