import requests
import os

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
key = 'trnsl.1.1.20180416T200439Z.5b8321e7af5487c7.9904804fd19a866ff7b916b509044e694f6d1131'


def define_path(file_name):
    file_path = f'{os.getcwd()}\\' + file_name + '.txt'
    output_path = f'{os.getcwd()}\\' + 'translate_{}.txt'.format(file_name)
    return file_path, output_path


def translate_it(file_path, from_lang, to_lang, output_path):
    with open(file_path, 'rb') as f:
        text = f.read()
        params = {
            'key': key,
            'lang': '{}-{}'.format(from_lang, to_lang),
            'text': text,
        }
        response = requests.get(url, params=params).json()
        with open(output_path, 'w', encoding='UTF-8') as f:
            f.write(''.join(response.get('text', [])))


files = ['DE', 'ES', 'FR']
for file in files:
    print(translate_it(define_path(file)[0], file.lower(), 'ru', define_path(file)[1]))
