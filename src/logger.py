import re
import time
import requests

from src import config as cfg


def log_event(text):
    event = '%s >> %s' % (time.ctime(), text)
    try:
        f = open('log.log', 'a', encoding='utf-8')
        f.write(event + '\n')
    except Exception as e:
        print("Проблемы с файлом: %s" % e)
    print(event)


def ask_log(message):
    if re.search('^sir_send_me_log_file_please$', message['text']):
        request = requests.post(
            cfg.URL + cfg.TOKEN + '/sendDocument',
            files={'document': open('log.log', 'rb')},
            data={'chat_id': message['chat']['id']},
        )
        if not request.status_code == 200:
            return False
        return request.json()['ok']
    if re.search('^sir_clear_log_please$', message['text']):
        open('log.log', 'w', encoding='utf-8')
        request = requests.post(cfg.URL + cfg.TOKEN + '/sendMessage', data={
            'chat_id': message['chat']['id'],
            'text': "Логи почищены. Начнем с начала?"
        })
        if not request.status_code == 200:
            return False
        return request.json()['ok']
