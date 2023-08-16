from text import TEXT_DICT as TEXT, STICKERS_DICT as STICKER, MSG_DICT as MSG
from keyboards import KEYBOARDS as KB
from keyboards import main_markup, photo_markup
from telegram.ext import MessageHandler, CommandHandler, filters
import random
import os
from utils import speech_to_text
from logger import setup_logger
import re

# инициируем логгер
logger = setup_logger(__name__)

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
    '''Функция для хэндлера отправки фотографий'''
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


async def voice_message(update, context):
    # получить объект аудио из сообщения пользователя
    voice = update.message.voice

    # сохранить аудиофайл
    file_path = f"audio_{voice.file_unique_id}.oga"
    file = await voice.get_file()
    await file.download_to_drive(file_path)

    # применить функцию распознавания речи
    try:
        text = speech_to_text(file_path)
    except:
        logger.error('Не удалось получить контент из аудиособщения')
        # отправить текст о том, что бот не понял, что в аудиосообщении
        await context.bot.send_sticker(chat_id=update.effective_chat.id,
                                   sticker=STICKER['error'])
        await update.message.reply_text(TEXT['what'])
    else:
        # обработать полученное сообщение
        await update.message.reply_text(TEXT['repeat'].format(text))
        if re.search(MSG['gpt'], text, flags=re.IGNORECASE):
            # отправить аудио-ответ про чат-гпт
            await context.bot.send_audio(chat_id=update.effective_chat.id,
                                 audio=open('./media/audio/gpt.ogg', 'rb'))
        elif re.search(MSG['sql'], text, flags=re.IGNORECASE):
            # отправить аудио-ответ про сравнение sql и nosql
            await context.bot.send_audio(chat_id=update.effective_chat.id,
                                 audio=open('./media/audio/sql.ogg', 'rb'))
        elif re.search(MSG['love'], text, flags=re.IGNORECASE):
            # отправить аудио-ответ про любовь
            await context.bot.send_audio(chat_id=update.effective_chat.id,
                                 audio=open('./media/audio/love.ogg', 'rb'))
        else:
            # отправить аудио-ответ про то, что ничего не понял
            await context.bot.send_sticker(chat_id=update.effective_chat.id,
                                   sticker=STICKER['error'])
            await context.bot.send_audio(chat_id=update.effective_chat.id,
                                 audio=open('./media/audio/error.ogg', 'rb'))
    print(text)
    # удалить временные аудиофайлы
    os.remove(file_path)
    os.remove(file_path[0:-3] + 'wav')

voice_message_handler = MessageHandler(filters.VOICE, voice_message)