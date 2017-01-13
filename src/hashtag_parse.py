import random
import re
import sqlite3
import src.config as cfg


def hashtag_parse(message, from_id, chat_id):
    con = sqlite3.connect('db/main_base.db')
    cur = con.cursor()
    reply = ' '

    if from_id in cfg.ADMIN_ID and re.search("#важно", message):
        cur.execute("INSERT INTO important (id, chat_id, text) VALUES(NULL, %s, '%s')" % (
            chat_id,
            message.replace("#важно ", '')
        ))
        con.commit()
        reply = random.choice([
            "Ууу, какая новость!",
            "Ну ничего себе.",
            "Новость добавлена."
        ])

    return reply
