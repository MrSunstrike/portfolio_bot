from telegram import ReplyKeyboardMarkup as RKM

KEYBOARDS = {
    'main': [
        ["Пришли своё фото"],
        ["Пришли эссе о своём увлечении"],
        ["Если бот не понимает сообщений"],
        ],

    'photo': [
        ["Школьное фото"],
        ["Последнее селфи"],
        ["Фото с детьми"],
        ["Вернуться назад"]
        ]
}

main_markup = RKM(KEYBOARDS['main'], one_time_keyboard=False)
photo_markup = RKM(KEYBOARDS['photo'], one_time_keyboard=False)