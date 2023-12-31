TEXT_DICT = {
    'hi1': 'Привет! Очень рад, что дали мне шанс! Не терпится показать Вам '
    'моё тестовое задание.',

    'hi2': 'С помощью кнопок, Вы можете запросить мои фотографии и краткое '
    'эссе о моём увлечении',

    'hi3': 'Также бота можно попросить текстом или голосом отправить мои '
    'аудиоответы на вопросы про: GPT, разницу SQL и NoSQL, историю любви',

    'docs': 'Если у Вас так и не получилось, выпросить у бота мои голосовые '
    'сообщения на заданные темы, то мне придется открыть капот и показать '
    'Вам немного внутренностей бота.\n\nЧтобы отправить Вам необходимое '
    'голосовое сообщение, бот ищет в Ваших сообщениях (текстовых или '
    'голосовых) соответствующие ключи:\n\n- Для отправки войса про GPT: <i>'
    'gt, gpt, гпт, чат, баб</i>\n- Для отправки войса про разницу SQL и '
    'NoSQL: <i>sql, бд, баз, данных, разниц, различ, отлич</i>\n- Для '
    'отправки войса про историю любви: <i>любов, любв, истор</i>\n\nНапишите '
    'или надиктуйте боту сообщение с использованием данных ключей и '
    'обязательно получите ответ.\n\n<i>p.s. Сожалею, что пришлось '
    'объяснять</i>',

    'photo': 'Фотографию? Не вопрос!\nКакую Вам отправить?',

    'back': 'Окей, никаких фотографий! Тогда что?',

    'what': 'К сожалению, не понял вас. Попробуйте перед записью немного '
    'подождать - 1 секундочку. У меня есть некоторые проблемы с пониманием '
    'первых и последних слов - это особенность библиотек, которые я использую.'
    '\nСпасибо за понимание!',

    'repeat': 'Вот, что я услышал:\n«{}»',

    'essay': 'Моё главное увлечение на протяжении уже года - '
    '<b>программирование</b>!\n\nГод назад я вывел в консоль свой первый '
    '<code>Hello, World!</code>, и с тех пор всё никак не могу остановиться. '
    'Строчка за строчкой пополняется мой репозиторий, библиотека за '
    'библиотекой расширяется мой технологический стек.\n\nЗа время обучения я '
    'написал несколько интересных проектов:\n\n<i>- Корпоративный портал для '
    'сотрудников моего департамента\n- Социальная сеть для друзей\n'
    '- API-сервис для стандартизации адресов\n- Дэйли-бот для Telegram\n'
    '- Этот замечательный бот-портфолио</i>\n\nВ процессе обучения я понял, '
    'что профессия разработчика - это не только про написание кода, но и его '
    'отладку, оптимизацию, работу с кодом других программистов, '
    'версионирование кода, тестирование, а также деплой своих приложений и '
    'работа над их инфраструктурой на серверах.\n\n<i>Программирование - '
    'уникальный и безграничный мир, который открывает новые крутые '
    'возможности. Буду очень рад провести в этот мир таких же жаждущих знаний '
    'ребят!</i>',

    'school': 'Это мои школьные годы. В этой категории 10 фотографий',

    'selfie': 'Это одно из последних селфи. В этой категории 6 фотографий',

    'work': 'Это фото из Артека. В этой категории 10 фотографий',

    'error': 'К сожалению, я не могу обработать эту команду. Возможно, я '
    'неправильно распознал Ваше голосовое сообщение или просто не могу '
    'понять, что Вы написали:(\n\nВоспользуйтесь специальной кнопкой в меню, '
    'чтобы получить подсказку, как меня использовать.',

    'rep': '<a href="https://github.com/MrSunstrike/portfolio_bot">'
    'РЕПОЗИТОРИЙ БОТА</a>'
}

STICKERS_DICT = {
    'hi': 'CAACAgIAAxkBAAEJpH5kqrk26qdTl0UWLDbeog8-RoAn2wACbwAD29t-AAGZW1Coe5O'
    'AdC8E',

    'error': 'CAACAgIAAxkBAAEJpIBkqru4GP4UMEIVHkNcU1A9-6lhRgACYwAD29t-AAGMnQU9'
    '50KD5y8E',

    'like': 'CAACAgIAAxkBAAEJpIJkqrvBHIxzZuOxRdTz0zIxNivyxQACPwAD29t-AAH05pw4A'
    'eSqaS8E',

    'thinks': 'CAACAgIAAxkBAAEJpIRkqrvQHG92ZAe9fIDUmhcLneAn_gACXwAD29t-AAGEsFS'
    'bEa7K4y8E',

    'kiss': 'CAACAgIAAxkBAAEJpIZkqrzAfNUTJvqhj5JfwKKvbcwMrAACZAAD29t-AAFfuVWO-'
    'HpEki8E',

    'cute': 'CAACAgIAAxkBAAEJpHxkqriX-JGw4-qgjK_FIgt0f0uLaAACbQAD29t-AAF1HuyF8'
    'vtEpS8E'
}

MSG_DICT = {
    'gpt': '(^.*gt.*$|^.*gpt.*$|^.*гпт.*$|^.* чат.*$|^.*баб.*$)',
    'sql': '(^.*sql.*$|^.*бд.*$|^.*баз.*$|^.*данных.*$|^.*разниц.*$|^.*отлич.*'
    '$|^.*различ.*$)',
    'love': '(^.*любов.*$|^.*любв.*$|^.*истор.*$)'
}
