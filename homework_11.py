import json


def calculate_words_in_newsafr():
    global ranging_afr_sort
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


calculate_words_in_newsafr()


def calculate_words_in_newscy():
    with open('newscy.json', encoding='UTF-8') as f:
        cy = json.load(f)
        cy_data = []
        for item in cy["rss"]["channel"]["items"]:
            cy_data.append(item['description'].split(' '))
        cy_word_list = []
        for data in cy_data:
            for element in data:
                cy_word_list.append(element)
        ranging_cy = dict()
        for i, word in enumerate(cy_word_list):
            ranging_cy.setdefault(len(cy_word_list[i]), [])
            ranging_cy[len(cy_word_list[i])].append(word)
            ranging_cy_sort = sorted(ranging_cy.keys(), reverse=True)
        for data in ranging_cy_sort[0:10]:
            print(data, ranging_cy[data])
        print('\n')


calculate_words_in_newscy()


def calculate_words_in_newsfr():
    with open('newsfr.json', encoding='cp1251') as f:
        fr = json.load(f)
        fr_data = []
        for item in fr["rss"]["channel"]["items"]:
            fr_data.append(item['description'].split(' '))
        fr_word_list = []
        for data in fr_data:
            for element in data:
                fr_word_list.append(element)
        ranging_fr = dict()
        for i, word in enumerate(fr_word_list):
            ranging_fr.setdefault(len(fr_word_list[i]), [])
            ranging_fr[len(fr_word_list[i])].append(word)
            ranging_fr_sort = sorted(ranging_fr.keys(), reverse=True)
        for data in ranging_fr_sort[0:10]:
            print(data, ranging_fr[data])
        print('\n')


calculate_words_in_newsfr()


def calculate_words_in_newsit():
    with open('newsit.json', encoding='UTF-8') as f:
        it = json.load(f)
        it_data = []
        for item in it["rss"]["channel"]["items"]:
            it_data.append(item['description'].split(' '))
        it_word_list = []
        for data in it_data:
            for element in data:
                it_word_list.append(element)
        ranging_it = dict()
        for i, word in enumerate(it_word_list):
            ranging_it.setdefault(len(it_word_list[i]), [])
            ranging_it[len(it_word_list[i])].append(word)
            ranging_it_sort = sorted(ranging_it.keys(), reverse=True)
        for data in ranging_it_sort[0:10]:
            print(data, ranging_it[data])
        print('\n')


calculate_words_in_newsit()
