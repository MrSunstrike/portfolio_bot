from text import TEXT_DICT as TEXT
from keyboards import main_markup, photo_markup
from telegram.ext import MessageHandler, CommandHandler, filters

async def start(update, context):
    await update.message.reply_text(TEXT['hi1'])
    await update.message.reply_text(TEXT['hi2'])
    await update.message.reply_text(TEXT['hi3'], reply_markup=main_markup)

start_handler = CommandHandler('start', start)