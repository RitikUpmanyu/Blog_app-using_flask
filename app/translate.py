import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['YANDEX_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json'
                     '/translate?key={}&text={}&lang={}-{}'.format(
                         current_app.config['YANDEX_TRANSLATOR_KEY'],text, source_language, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    returned = json.loads(r.content.decode('utf-8-sig'))
    list_text = returned.get('text')
    return list_text[0]
