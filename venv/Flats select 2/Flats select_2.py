import csv
import random

flats_list = list()

with open('output.csv', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)


# TODO 1:
# Напишите цикл, который проходит по всем квартирам, и печатает только новостройки
# и их порядковые номера в файле. Подсказка:

print('Задание 1')
quantity_of_newbuilds = 0
newbuild_list = list()
for i, flat in enumerate(flats_list):
    if "новостройка" in flat:
        quantity_of_newbuilds += 1  # считаю кол-во новостроек
        newbuild_list.append(flats_list[i])  # собираю список новостроек
        print(i, flat[
                 0:5])  # здесь решил не выводить всю инфу по новостройкам, а взял
        # только первые 6 элементов для компактности вывода
print('Всего новостроек: {0}'.format(quantity_of_newbuilds))

# TODO 2:
# При помощи пересечения множеств попробуйте сравнить больше двух новостроек между собой одновременно
# например, пересечение 3 и 6 квартиры из файла с ЦИАНа делается так:
print('Задание 2')
for i, newbuild in enumerate(newbuild_list):
    a = [random.randint(0, quantity_of_newbuilds - 1) for _ in range(3)]
    flats_intersesction = set(newbuild_list[a[0]]) & set(newbuild_list[a[1]]) & set(
        newbuild_list[a[2]])  # сравниваю рандомные 3 новостройки
    print('Результат {}:'.format(i + 1), flats_intersesction)

# Порядковые номера новостроек вы уже получили при выполнении предыдущего задания.
# Не забудьте вывести результат функцией print

# TODO3:
# Вот так мы превратили наш массив квартир в словарь, где ключом является уникальный номер объявления,
# а значением - ссылка на страничку с объявлением.
# Измените код так, чтобы стало наоборот.
print('Задание 3')
test_dict = dict()
for i, flat in enumerate(flats_list):
    if i == 0:
        continue
    # test_dict[flat[0]] = flat[len(flat)-1] # ключ - номер объявления, значение - ссылка
    test_dict[flat[len(flat) - 1]] = flat[0]  # ключ - ссылка, значение - номер объявления
print(test_dict)

