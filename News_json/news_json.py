import chardet
import json
from pprint import pprint

with open("newsfr.json") as f:
    news = json.load(f)
    pprint(news)


#
# def top10_words_in_article(a):  # функция поиска топ-10 слов в статье
#     with open(a, 'rb') as f:
#         data = f.read()
#         result = chardet.detect(data)
#         s = data.decode(result['encoding'])
#         list_with_words = s.split(' ')  # из строки делаем список с элементами-словами
#         worddict = {}
#         for i, k in enumerate(list_with_words):  # наполняем словарь парами "слово:кол-во вхождений в статью"
#             if len(list_with_words[i]) > 6:
#                 if list_with_words[i] not in worddict:
#                     worddict[list_with_words[i]] = 1
#                 elif list_with_words[i] in worddict:
#                     worddict[list_with_words[i]] += 1
#         words = []
#         count_words = []
#         for i, k in worddict.items():  # из словаря делаем 2 списка - со словами и кол-вом вхождений
#             count_words.append(worddict[i])
#             words.append(i)
#         count_words = list(set(count_words))  # убираем дубли кол-ва вхождений
#         count_words.sort()  # сортируем по возрастанию
#         count_words.reverse()  # сортируем по убыванию
#         top_10 = count_words[:10]  # оставляем только 10 максимальных значений
#         for i in top_10:  # выводим слова, у которых значения в словаре соответствуют максимальным
#             top = i
#             for key, v in worddict.items():
#                 if top == worddict[key]:
#                     print('Слово {} встречается {} раз'.format(key, top))
#
#
# print('Топ-10 слов в статье newsafr:')
# print(top10_words_in_article('newsafr.txt'))
# print('Топ-10 слов в статье newscy:')
# print(top10_words_in_article('newscy.txt'))
# print('Топ-10 слов в статье newsfr:')
# print(top10_words_in_article('newsfr.txt'))
# print('Топ-10 слов в статье newsit:')
# print(top10_words_in_article('newsit.txt'))
