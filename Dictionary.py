# Задача 1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя
# владельца и номер полки, на котором он будет храниться
# Задача №2. Дополнительная (не обязательная)
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;


documents = [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
             {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
             {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}]
directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}

print('Выберите действие:')
print('р - вывод имени человека по документу')
print('l - вывод списка всех документов')
print('s - вывод номера полки документа')
print('а - добавление нового документа')


def name_by_number(a):  # команда 'p' - функция вывода имени по документу
    print(
        'Выберите цифру документа для вывода имени:')  # здесь упрощаем жизнь пользователю,
    # выводя весь список, и просим ввести порядковый номер документа
    for i, doc in enumerate(a):
        print('Документ {}:'.format(i), doc['number'])
    inp_doc = int(input())
    print(a[inp_doc]['name'])


def list_of_all(a):  # команда 'l' - функция вывода всего списка документов
    print('Перечень документов')
    for doc in a:
        print(doc['type'], doc['number'], doc['name'])


def shelf_number(a, b):  # команда 's' - функция вывода номера полки по документу
    print(
        'Введите номер документа из указанных ниже:')  # тут мы не упрощаем жизнь пользователю, но четко решаем
    # поставленную задачу))
    for i, doc in enumerate(a):
        print('Документ {}:'.format(i), doc['number'])
    inp_doc = input()
    for k, v in b.items():
        if inp_doc in v:
            print('Документ хранится на полке', k)


def add_document(a, b):
    print('Введите номер документа для добавления')
    inp_number = input()
    print('Введите тип документа для добавления')
    inp_type = input()
    print('Введите имя владельца документа для добавления')
    inp_name = input()
    print('Введите номер полки хранения документа для добавления')
    inp_shelf = input()
    a.append({'type': inp_type, 'number': inp_number, 'name': inp_name})
    b[inp_shelf].append(inp_number)
    print(a)
    print(b)


inp = input()
if inp == 'p':
    name_by_number(documents)
elif inp == 'l':
    list_of_all(documents)
elif inp == 's':
    shelf_number(documents, directories)
elif inp == 'a':
    add_document(documents, directories)
elif inp == 'd':
    print('Введите номер документа для удаления:')
    for i, doc in enumerate(documents):
        print('Документ {}:'.format(i), doc['number'])
    inp_doc = input()
    for i, dic in enumerate(documents):
        if inp_doc in dic:
            documents.pop([i])
            print(documents)

# print(documents,directories) # тут всега вывожу данные для проверки изменений


