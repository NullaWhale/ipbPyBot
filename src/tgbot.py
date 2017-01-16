import re

import src.config as cfg
import requests
from src.command_parse import command_parse
from src.logger import log_event, ask_log
from src.parse import parse

from src.hashtag_parse import hashtag_parse

offset = 0
message_counter = 0


def send(chat_id, text, reply_id=''):
    if re.findall('^is_sticker_', text):
        data = {
            'chat_id': chat_id,
            'sticker': re.findall('[^is_sticker_].*', text),
            'reply_to_message_id': reply_id
        }
        request = requests.post(cfg.URL + cfg.TOKEN + '/sendSticker', data=data)
    else:
        data = {
            'chat_id': chat_id,
            'text': text,
            'reply_to_message_id': reply_id,
            'parse_mode': 'HTML'
        }
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

        if 'message' in update and 'new_chat_member' in update['message']:
            send(update['message']['chat']['id'], "En taro " + update['message']['new_chat_member']['first_name'])

        if 'message' not in update or 'text' not in update['message']:
            log_event('Unknown message: %s' % update)
            continue

        chat = update['message']['chat']
        chat_id = update['message']['chat']['id']
        from_id = update['message']['from']['id']
        message_id = update['message']['message_id']
        message = update['message']['text']
        first_name = update['message']['from']['first_name']
        p_message = parse(message)

        if from_id is cfg.CREATOR: ask_log(update['message'])

        if re.search('^#', message, re.IGNORECASE):
            send(chat_id, hashtag_parse(message, from_id, chat_id))
        elif re.search('^/', message, re.IGNORECASE):
            send(chat_id, command_parse(message, chat))
        else:
            send(chat_id, p_message, message_id)

        if update['message']['chat']['type'] == 'private':
            log_event('#chat:%s#: %s (%s): "%s"' % (chat_id, first_name, from_id, message))
        else:
            log_event('#chat:%s#: %s (%s): "%s"' % (chat_id, first_name, from_id, message))

        log_event("BOT: \"%s\"" % p_message)


if __name__ == "__main__":
    while True:
        try:
            check_updates()
        except KeyboardInterrupt:
            print('Прервано пользователем.')
            break
