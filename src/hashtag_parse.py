import re
import sqlite3

import src.config as cfg


def hashtag_parse(message, from_id):
    con = sqlite3.connect('db/main_base.db')
    cur = con.cursor()
    reply = ' '

    if from_id == cfg.ADMIN_ID and re.search("#важно", message):
        cur.execute("INSERT INTO important (id, text) VALUES(NULL, '%s')" % message.replace("#важно ", ''))
        con.commit()

    return reply
