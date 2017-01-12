import re
import sqlite3
import github


def command_parse(message):
    con = sqlite3.connect('db/main_base.db')
    cur = con.cursor()
    reply = ' '

    if re.search('^/important', message, re.IGNORECASE):
        cur.execute('SELECT text FROM important')
        row = [st[0] for st in cur.fetchall()]
        if row:
            reply = "<b>Важные новости за последнее время:</b>\n"
            for item in row:
                reply += "—<i>" + item + "</i>\n"
        else:
            reply = "<b>Давно ничего важного небыло</b>"

    if re.search('/user_repos', message, re.IGNORECASE):
        git = github.Github()
        try:
            if message == '/user_repos':
                reply = "Юзернейм-то укажи мне, дурёха."
            else:
                user = git.get_user(message.replace("/user_repos ", ''))
                for repo in user.get_repos():
                    print(repo)
                    if repo.fork:
                        reply += "<i>id " + str(repo.id) + "</i> : <b>" + repo.full_name + "</b> <i>(fork)</i>\n"
                    else:
                        reply += "<i>id " + str(repo.id) + "</i> : <b>" + repo.full_name + "</b> \n"
        except:
            reply = "Чего-то ты не то ввел, дружище."

    if re.search('^/man', message, re.IGNORECASE):
        reply = "<a href=\"https://github.com/NullaWhale/ipbPyBot/blob/master/README.md\">Вот тут</a> все написано"

    return reply
