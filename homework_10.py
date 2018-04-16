import chardet

def calc_top_10_words_by_len(file_name):
    with open('{}.txt'.format(file_name), 'rb') as f:
        text = f.read()
        text_type = chardet.detect(text)
        text_str = text.decode(text_type['encoding'])
        text_list = text_str.split(' ')
        for i in text_list:
            if '\n' in i:
                text_list.remove(i)
                text_list.append(i[1:])
        ranging_text = dict()
        for i, word in enumerate(text_list):
            ranging_text.setdefault(len(text_list[i]), [])
            ranging_text[len(text_list[i])].append(word)
        ranging_text_sort = sorted(ranging_text.keys(), reverse=True)
        for data in ranging_text_sort[0:10]:
            if data >= 6:
                print(data, ranging_text[data])
        print('\n')


files = ['newsafr', 'newscy', 'newsfr', 'newsit']

for file in files:
    calc_top_10_words_by_len(file)