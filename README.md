# Бот-портфолио Mr.Sunstrike

_Тестовое задание от Яндекс Практикума на должность "Наставник на курсы для подростков по Python-разработке"_

## Как пользоваться ботом?

### 1. С помощью кнопок
    - "Пришли своё фото" - вызывает следующую клавиатуру выбора категории фотографий:
        - "Школьное фото" - отправит случайную фотографию из папки моих школьных фотографий
        - "Последнее селфи" - отправит случайную фотографию из папки, в которой я собрал несколько своих последний себяшек
        - "Фото с детьми" - отправит случайную фотографию из папки "Артек, 2015" - там я в роли вожатого и мои счастливые дети
        - "Вернуться назад" - вернет начальную клавиатуру. Это когда вы наиграете с вызововм моих фотографий с разных категорий.
    - "Пришли эссе о своём увлечении" - бот отправит вам мое эссе на тему моего увлечения. В этом сообщении будет применено html-форматироввание.
    - "Если бот не понимает сообщений" - отправит краткую инструкцию, как наверняка вызвать мои голосовые сообщения на заданные темы. Я надеюсь, что эта кнопка Вам не пригодится.
    - "Репозиторий бота" - бот отправит Вам ссылку на свой репозиторий
### 2. С помощью текстовых сообщений
    Спросите у бота, как бы он объяснил бабушке что такое GPT или в чем отличие SQL от NoSQL, ну или пусть поделится историей первой любви - он обязательно отправит вам соответствующее голосовое сообщение.
### 3. С помощью голосовых сообщений
    Всё то же самое, что и с текстовыми сообщениями, но с помощью войсов. Задайте свой вопрос с помощью голосового сообщений и бот обязательно ответит. В коде используются не прорывные API-сервисы, а более простые библиотеки, поэтому бот может немного тупить - просто попросите его еще раз, сделав небольшие паузы в начале и в конце Вашего голосового сообщения.

## Структура проекта

- `main.py` - модуль основной логики проекта, используется для запуска бота;
- `handlers.py` - логика всех ручек бота прописана в этом модуле;
- `utils.py` - модуль для функции конвертирования голосовых сообщений в нужный аудиоформат и распознания речи;
- `keyboards.py` - в этом модуле описаны используемые в боте клавиатуры;
- `text.py` - все текстовые формулировки, а также стикеры находятся в этом модуле;
- `logger.py` - модуль, в котором прописана логика логгера и функция инициирования локальных логгеров внутри других модулей.

## Установка проекта

1. Клонируйте репозиторий: `git@github.com:MrSunstrike/portfolio_bot.git` на ваше устройство.
2. Cоздайте виртуальное окружение, активируйте его и установите зависимости: `pip install -r requirements.txt`
3. Установите на Ваш компьютер приложение FFmpeg - оно необходимо для корректной работы библиотеки `pydub` (для конвертирования голосового сообщения в нужный формат):
    - Для Windows:
        1. Перейдите на официальный сайт FFmpeg по адресу https://ffmpeg.org и перейдите на страницу "Download".
        2. Перейдите в раздел "Windows Builds" и найдите ссылку на последний статический бинарный файл для Windows.
        3. Скачайте архив, распакуйте его и сохраните его в удобном для вас месте.
        4. Добавьте путь к каталогу FFmpeg в переменную среды PATH. Вы можете сделать это следующим образом:
            - Нажмите правой кнопкой мыши на значок "Мой компьютер" и выберите "Свойства".
            - Перейдите во вкладку "Дополнительные параметры системы".
            - Нажмите на кнопку "Переменные среды".
            - В разделе "Переменные среды пользователя" найдите переменную PATH и нажмите на кнопку "Изменить".
            - Добавьте полный путь к каталогу FFmpeg, который вы распаковали, в список переменных PATH.
            - Нажмите "ОК" до закрытия всех диалоговых окон.
    - Для macOS:
        1. Откройте Terminal (Терминал) на вашем Mac.
        2. Установите Homebrew, если у вас его нет. Вы можете сделать это, введя в терминале следующую команду и следуя инструкциям установщика: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
        3. После установки Homebrew введите в терминале следующую команду для установки FFmpeg: `brew install ffmpeg`
    - Для Linux:
        1. Обновите список пакетов: `sudo apt update`
        2. Установите FFmpeg: `sudo apt install ffmpeg`
4. Создайте файл `.env` в корневой директории проекта и задайте значение переменной окружения:
    - `BOT_TOKEN` - идентификатор вашего бота в Telegram, необходимый для взаимодействия с ним. Получить можно у `@BotFather` в Telegram
5. Запустите бота с помощью команды `python main.py`

## Лицензия

Проект лицензирован в соответствии с лицензией [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

## Автор

Автор проекта - Mr.Sunstrike

  - Email: misha@mrsunstrike.ru
  - GitHub: [github.com/MrSunstrike](https://github.com/MrSunstrike)