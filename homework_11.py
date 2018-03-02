import chardet
import json


def calculate_words_in_newsafr():
    with open('newsafr.json', 'rb') as f:
        afr = json.load(f)
        afr_data = []
        for item in afr["rss"]["channel"]["items"]:
            afr_data.append(item['description'].split(' '))
        word_list = []
        for data in afr_data:
            for element in data:
                word_list.append(element)
        ranging_afr = dict()
        for i, word in enumerate(word_list):
            ranging_afr.setdefault(len(word_list[i]), [])
            ranging_afr[len(word_list[i])].append(word)
            ranging_afr_sort = sorted(ranging_afr.keys(), reverse=True)
        for data in ranging_afr_sort[0:10]:
            print(data, ranging_afr[data])
        print('\n')
