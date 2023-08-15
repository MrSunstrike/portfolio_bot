from telegram import ReplyKeyboardMarkup as RKM

KEYBOARDS = {
    'main': [
        ["Пришли своё фото"],
        ["Пришли эссе о своём увлечении"],
        ],

    'photo': [
        ["Школьное фото"],
        ["Последнее селфи"],
        ["Фото с детьми"],
        ]
}

main_markup = RKM(KEYBOARDS['main'], one_time_keyboard=False)
photo_markup = RKM(KEYBOARDS['photo'], one_time_keyboard=False)