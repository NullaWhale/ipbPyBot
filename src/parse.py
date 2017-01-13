import random
import re
import time
import src.config as cfg


def parse(message):
    reply = ' '

    if re.search('красота', message, re.IGNORECASE):
        reply = "Согласен, красивая картина."

    elif re.search('питон|python', message, re.IGNORECASE):
        reply = random.choice([
            "@movax0 очень любит питон",
            "Папа ^_^",
            "is_sticker_BQADAgADxCsAAktqAwABh9k43RMGQ5YC"
        ])

    elif re.search('^date|дата$', message, re.IGNORECASE):
        reply = time.ctime(time.time())

    elif re.search('^time|время$', message, re.IGNORECASE):
        reply = time.ctime(time.time())

    elif re.search('Капитан,|Кэп,|Куп,|Пирожок,', message, re.IGNORECASE):
        reply = random.choice([
            "Тащи пирожки",
            "Готовьте лодку!",
            "Капитан на борту!",
            "Лодка подана!",
            "Ваш корабль подан, Капитан",
            "O Captain! my Captain!"
        ])
    elif re.search('^Дувел,|Пувел,', message, re.IGNORECASE):
        reply = random.choice([
            "Как иголка в стоге сена",
            "Охохохохо"
        ])

    elif re.search('Мукс[аеу]?(,)?', message, re.IGNORECASE):
        reply = random.choice([
            "Муксус-бамбуксус"
        ])

    elif re.search('Даня,|Даниил,|Старост[ауойе]', message, re.IGNORECASE):
        reply = random.choice([
            cfg.ADMIN_NAME + " в данный момент отсутствует. \n"
            "Если это важно, оставьте свое сообщение с пометкой #важное",
            "Все ищем старосту!"
        ])

    elif re.search('^добро|все|ребя', message, re.IGNORECASE):
        reply = random.choice([
            "И тебе доброго утра!",
            "Добрейшего тебе предрассветного утра!"
        ])

    elif re.search('^ку|прив|здаров', message, re.IGNORECASE):
        reply = random.choice([
            "Здарова",
            "Привет-привет",
            "Ну здравствуй, проходи, не стой на пороге",
            "Здарова, коль не шутишь"
        ])

    elif re.search('Бот,', message, re.IGNORECASE):
        reply = random.choice([
            "Сам ты бот, я человек",
            "Ну ты и мр*зь",
            "Я сейчас закричу!"
        ])

    elif re.search('2007(?:[мй]|ого|ому)?', message, re.IGNORECASE):
        reply = random.choice([
            "Никто и никогда не вернет 2007-й год",
            "Сентяяябрь гориит",
            "За что теперь тебя любить?",
            "Зачем я должен верить в тебя?",
            "...осколками наших разбитых сердец",
            "Мы с тобой вулканы",
            "Это просто дождь",
            "Я плаачу и вместе с тем умираю",
            "Остальное забыл навсегда",
            "Поцелуй из огня!"
        ])

    return reply
