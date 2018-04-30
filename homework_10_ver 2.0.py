import chardet


def calc_top_10_words_by_occurence(file_name):
    with open('{}.txt'.format(file_name), 'rb') as f:
        text = f.read()
        text_type = chardet.detect(text)
        text_str = text.decode(text_type['encoding'])
        words_list = text_str.split(' ')
        for i in words_list:
            if '\n' in i:
                words_list.remove(i)
                words_list.append(i[1:])
        words_list_over_6 = []
        for i in words_list:
            if len(i) >= 6:
                words_list_over_6.append(i)
        unique_words = dict()
        for word in words_list_over_6:
            if word not in unique_words.keys():
                unique_words[word] = 0
        for key in unique_words.keys():
            for word in words_list_over_6:
                if key == word:
                    unique_words[key] += 1
        unique_words_sort = sorted(unique_words.values(), reverse=True)
        words_for_print = dict()
        for count in unique_words_sort[0:10]:
            for key, value in unique_words.items():
                if value == count:
                    words_for_print[key] = count
        for key, value in words_for_print.items():
            print(key, ": ", value)
        print('\n')


files = ['newsafr', 'newscy', 'newsfr', 'newsit']


for file in files:
    calc_top_10_words_by_occurence(file)
