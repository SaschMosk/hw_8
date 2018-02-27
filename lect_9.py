# f = open('hell', 'rt')
# print(f.read())
# print(f.readline())

# with open('hell') as f:
#     print(f.read())
# print('fail zakrit {}'.format(f.closed))

# например, сколько раз Пьер и Наташа встретились в одном абзаце в войне и мире
# count = 0
# with open('_') as f:
#    for line in f:
#        if 'Наташ' in line and 'Пьер' in line:
#            count += 1
#            print(line, end='')
# print('Наташа и Пьер упоминались вместе в {} абзацах'.format(count))

# другой пример оценки
best_grade = None
best_rating = None
# извлечение классов с оценками по отдельности
with open('scores') as f:
    for line in f:
        grade = line.strip()
        scores = f.readline()
        f.readline()
        print('Класс {}, оценки: {}'.format(grade, scores))

        int_scores = []
        splitted = scores.split(' ')
        for i in splitted:
            int_scores.append(int(i))
        average = sum(int_scores) / len(int_scores)
        if best_rating is None or average > best_rating:
            best_rating = average
            best_grade = grade
print('Лучший класс {} с лучшей оценкой: {}'.format(best_grade, best_rating))

# время

from datetime import datetime
with open('write_res.txt', 'w') as f:
    f.write((str(datetime.now())))