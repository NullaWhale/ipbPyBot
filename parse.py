import random
import re
import time

import github


def parse(message):
    reply = ' '

    if re.search('красота', message, re.IGNORECASE):
        reply = "Согласен, красивая картина."

    if re.search('питон|python', message, re.IGNORECASE):
        reply = random.choice([
            "@movax0 очень любит питон",
            "Папа ^_^",
            "is_sticker_BQADAgADxCsAAktqAwABh9k43RMGQ5YC"
        ])

    if re.search('^date|дата$', message, re.IGNORECASE):
        reply = time.ctime(time.time())

    if re.search('^time|время$', message, re.IGNORECASE):
        reply = time.ctime(time.time())

    if re.search('^Капитан,|Кэп,|Куп,', message, re.IGNORECASE):
        reply = random.choice([
            "Тащите пирожки",
            "Готовьте лодку!",
            "Капитана на борт!",
            "Капитан на борту!",
            "Лодка подана!",
            "Ваш корабль подан, капитан",
            "O Captain! my Captain!"
        ])

    if re.search('^добро|все|ребя', message, re.IGNORECASE):
        reply = random.choice([
            "И тебе доброго утра!",
            "Добрейшего тебе предрассветного утра!"
        ])

    if re.search('^ку|прив|здаров', message, re.IGNORECASE):
        reply = random.choice([
            "Здарова",
            "Привет-привет",
            "Ну здравствуй, проходи, не стой на пороге",
            "Здарова, коль не шутишь"
        ])

    if re.search('Бот,', message, re.IGNORECASE):
        reply = random.choice([
            "Сам ты бот, я человек",
            "Ну ты и мр*зь",
            "Я сейчас закричу!"
        ])

    if re.search('2007(?:[мй]|ого|ому)?', message, re.IGNORECASE) or \
            re.search('дветысячиседьмой|дветысячисемь|дветысячи седьмой|дветысячи семь', message, re.IGNORECASE):
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

    if re.findall('^user_repos:', message, re.IGNORECASE):
        git = github.Github()
        try:
            user = git.get_user(re.findall('[^:].*', re.findall('[^user_repos].*', message)[0])[0])
            for repo in user.get_repos():
                print(repo)
                if repo.fork: reply += "id " + str(repo.id) + ": \"" + repo.full_name + "\" (fork)\n"
                else: reply += "id " + str(repo.id) + ": \"" + repo.full_name + "\" \n"
        except:
            reply = "Чего-то ты не то ввел, дружище. Попробуй-ка по другому как-нибудь."

    return reply
