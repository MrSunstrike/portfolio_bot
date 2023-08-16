import os
import random
import re

from telegram.ext import CommandHandler, MessageHandler, filters

from keyboards import KEYBOARDS as KB
from keyboards import main_markup, photo_markup
from logger import setup_logger
from text import MSG_DICT as MSG
from text import STICKERS_DICT as STICKER
from text import TEXT_DICT as TEXT
from utils import speech_to_text

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


async def send_docs(update, context):
    '''Функция для хэндлера, отправляющего доку'''
    await update.message.reply_text(TEXT['docs'],
                                    reply_markup=main_markup,
                                    parse_mode='html')

send_docs_handler = MessageHandler(
    filters.Regex(f"^{KB['main'][2][0]}$"), send_docs
)


async def get_back(update, context):
    '''Функция для хэндлера, возвращающего основную клавиатуру'''
    await update.message.reply_text(TEXT['back'], reply_markup=main_markup)

get_back_handler = MessageHandler(
    filters.Regex(f"^{KB['photo'][3][0]}$"), get_back
)


async def send_rep(update, context):
    '''Функция для хэндлера, отправляющего репозиторий бота'''
    await update.message.reply_text(TEXT['rep'],
                                    reply_markup=main_markup,
                                    parse_mode='html')

send_rep_handler = MessageHandler(
    filters.Regex(f"^{KB['main'][3][0]}$"), send_rep
)


async def send_voice(update, context):
    '''Функция для хэндлера, возвращающего основную клавиатуру'''
    text = update.message.text

    # путь к файлу ответа
    path = ''

    if re.search(MSG['gpt'], text, flags=re.IGNORECASE):
        path = './media/audio/gpt.ogg'
    elif re.search(MSG['sql'], text, flags=re.IGNORECASE):
        path = './media/audio/sql.ogg'
    elif re.search(MSG['love'], text, flags=re.IGNORECASE):
        path = './media/audio/love.ogg'
    else:
        await context.bot.send_sticker(chat_id=update.effective_chat.id,
                                       sticker=STICKER['error'])
        await update.message.reply_text(TEXT['error'])
    if path:
        await context.bot.send_audio(chat_id=update.effective_chat.id,
                                     audio=open(path, 'rb'))

send_voice_handler = MessageHandler(filters.TEXT, send_voice)


async def send_photo(update, context):
    '''Функция для хэндлера отправки фотографий'''
    if update.message.text == KB['photo'][0][0]:
        folder_path = "./media/img/school/"
        caption = TEXT['school']
    elif update.message.text == KB['photo'][1][0]:
        folder_path = "./media/img/selfie/"
        caption = TEXT['selfie']
    else:
        folder_path = "./media/img/work/"
        caption = TEXT['work']
    photos = os.listdir(folder_path)
    photo_path = os.path.join(folder_path, random.choice(photos))
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(photo_path, 'rb'),
                                 caption=caption)

send_photo_handler = MessageHandler(
    filters.Regex(
        f"^({KB['photo'][0][0]}|{KB['photo'][1][0]}|{KB['photo'][2][0]})$"
    ), send_photo
)


async def voice_message(update, context):
    # получить объект аудио из сообщения пользователя
    voice = update.message.voice

    # путь к файлу ответа
    path = ''

    # сохранить аудиофайл
    file_path = f"audio_{voice.file_unique_id}.oga"
    file = await voice.get_file()
    await file.download_to_drive(file_path)

    # применить функцию распознавания речи
    try:
        text = speech_to_text(file_path)
    except Exception:
        logger.error('Не удалось получить контент из аудиособщения')
        # отправить текст о том, что бот не понял, что в аудиосообщении
        await update.message.reply_text(TEXT['what'])
    else:
        logger.info(f'Контент получен: "{text}"')
        # обработать полученное сообщение
        await update.message.reply_text(TEXT['repeat'].format(text))
        if re.search(MSG['gpt'], text, flags=re.IGNORECASE):
            path = './media/audio/gpt.ogg'
        elif re.search(MSG['sql'], text, flags=re.IGNORECASE):
            path = './media/audio/sql.ogg'
        elif re.search(MSG['love'], text, flags=re.IGNORECASE):
            path = './media/audio/love.ogg'
        else:
            await context.bot.send_sticker(chat_id=update.effective_chat.id,
                                           sticker=STICKER['error'])
            await update.message.reply_text(TEXT['error'])
        if path:
            await context.bot.send_audio(chat_id=update.effective_chat.id,
                                         audio=open(path, 'rb'))

    # удалить временные аудиофайлы
    os.remove(file_path)
    os.remove(file_path[0:-3] + 'wav')

voice_message_handler = MessageHandler(filters.VOICE, voice_message)


async def send_essay(update, context):
    '''Функция для хэндлера, отправляющего эссе'''
    photo_path = './media/img/hrt.jpg'
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(photo_path, 'rb'),
                                 caption=TEXT['essay'],
                                 parse_mode='html')

send_essay_handler = MessageHandler(
    filters.Regex(f"^{KB['main'][1][0]}$"), send_essay
)
