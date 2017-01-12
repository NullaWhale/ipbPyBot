import re
import requests
import time

import config as cfg
from parse import parse
from command_parse import command_parse

offset = 0


def log_event(text):
    event = '%s >> %s' % (time.ctime(), text)
    print(event)


def send(chat_id, text, reply_id=''):
    if re.findall('^is_sticker_', text):
        data = {'chat_id': chat_id, 'sticker': re.findall('[^is_sticker_].*', text), 'reply_to_message_id': reply_id}
        request = requests.post(cfg.URL + cfg.TOKEN + '/sendSticker', data=data)
    else:
        data = {'chat_id': chat_id, 'text': text, 'reply_to_message_id': reply_id}
        request = requests.post(cfg.URL + cfg.TOKEN + '/sendMessage', data=data)
    if not request.status_code == 200:
        return False
    return request.json()['ok']


def check_updates():
    global offset

    data = {'offset': offset + 1, 'limit': 0, 'timeout': 0}

    try:
        request = requests.post(cfg.URL + cfg.TOKEN + '/getUpdates', data=data)
    except:
        log_event('Error getting updates')
        return False

    if not request.status_code == 200: return False
    if not request.json()['ok']: return False

    for update in request.json()['result']:
        offset = update['update_id']
        if 'message' not in update or 'text' not in update['message']:
            log_event('Unknown message: %s' % update)
            continue

        from_id = update['message']['chat']['id']
        message_id = update['message']['message_id']
        message = update['message']['text']
        first_name = update['message']['from']['first_name']
        p_message = parse(message)

        if re.search('^/', message, re.IGNORECASE):
            send(from_id, command_parse(message))

        send(from_id, p_message, message_id)

        if update['message']['chat']['type'] == 'private':
            parameters = (first_name, from_id, message)
            log_event('###: %s (%s): "%s"' % parameters)
        else:
            parameters = (first_name, from_id, message)
            log_event('###: %s (%s): "%s"' % parameters)

        log_event("BOT: \"%s\"" % p_message)


if __name__ == "__main__":
    while True:
        try:
            check_updates()
        except KeyboardInterrupt:
            print('Прервано пользователем..')
            break
