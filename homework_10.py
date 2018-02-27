import chardet

with open('newsafr.txt', 'rb') as f:
    afr = f.read()
    afr_type = chardet.detect(afr)
    afr_str = afr.decode(afr_type['encoding'])
    afr_list = afr_str.split(' ')
    ranging_afr = dict()
    for i, word in enumerate(afr_list):
        ranging_afr.setdefault(len(afr_list[i]), [])
        ranging_afr[len(afr_list[i])].append(word)
    ranging_afr_sort = sorted(ranging_afr.keys(), reverse=True)
    for data in ranging_afr_sort[0:10]:
        print(data, ranging_afr[data])
    print('\n')

with open('newscy.txt', 'rb') as k:
    cy = k.read()
    cy_type = chardet.detect(cy)
    cy_str = cy.decode(cy_type['encoding'])
    cy_list = cy_str.split(' ')
    ranging_cy = dict()
    for i, word in enumerate(cy_list):
        ranging_cy.setdefault(len(cy_list[i]), [])
        ranging_cy[len(cy_list[i])].append(word)
    ranging_cy_sort = sorted(ranging_cy.keys(), reverse=True)
    for data in ranging_cy_sort[0:10]:
        print(data, ranging_cy[data])
    print('\n')

with open('newsfr.txt', 'rb') as m:
    fr = m.read()
    fr_type = chardet.detect(fr)
    fr_str = fr.decode(fr_type['encoding'])
    fr_list = fr_str.split(' ')
    ranging_fr = dict()
    for i, word in enumerate(fr_list):
        ranging_fr.setdefault(len(fr_list[i]), [])
        ranging_fr[len(fr_list[i])].append(word)
    ranging_fr_sort = sorted(ranging_fr.keys(), reverse=True)
    for data in ranging_fr_sort[0:10]:
        print(data, ranging_fr[data])
    print('\n')

with open('newsit.txt', 'rb') as p:
    it = p.read()
    it_type = chardet.detect(it)
    it_str = it.decode(it_type['encoding'])
    it_list = it_str.split(' ')
    ranging_it = dict()
    for i, word in enumerate(it_list):
        word_len = len(it_list[i])
        ranging_it.setdefault(len(it_list[i]), [])
        ranging_it[len(it_list[i])].append(word)
    ranging_it_sort = sorted(ranging_it.keys(), reverse=True)
    for data in ranging_it_sort[0:10]:
        print(data, ranging_it[data])
    print('\n')
