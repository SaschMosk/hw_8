import requests

url = 'https://translate.yandex.net/api/v1/tr.json/translate?'

def translate_en_ru(text):
    response = requests.post(
        url,
        params=dict(
            id='3d587d02.5aa00a59.6600c133-2-0',
            srv='tr-text',
            lang='en-ru',
            reason='auto'
        ),
        data=dict(
            text=text
        )
    )

    return ''.join(response.json()['text'])

print(translate_en_ru("hello world"))