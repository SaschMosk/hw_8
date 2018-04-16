import json
import chardet

files = ['newsafr', 'newscy', 'newsfr', 'newsit']


def detect_type_json(file_name):
    with open('{}.json'.format(file_name), 'rb') as f:
        text = f.read()
        text_type = chardet.detect(text)
        return text_type


def calc_top_10_words_by_len(file_name, type):
    with open('{}.json'.format(file_name), encoding=type['encoding']) as f:
        text = json.load(f)
        text_data = []
        for item in text["rss"]["channel"]["items"]:
            text_data.append(item['description'].split(' '))
        text_list = []
        for data in text_data:
            for i in data:
                text_list.append(i)
        ranging_text = dict()
        for i, word in enumerate(text_list):
            ranging_text.setdefault(len(text_list[i]), [])
            ranging_text[len(text_list[i])].append(word)
            ranging_text_sort = sorted(ranging_text.keys(), reverse=True)
        for data in ranging_text_sort[0:10]:
            if data >= 6:
                print(data, ranging_text[data])
        print('\n')


for file in files:
    calc_top_10_words_by_len(file, detect_type_json(file))