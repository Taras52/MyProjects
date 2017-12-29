# Имеется группа студентов, у каждого из которых есть следующие характеристики: имя, фамилия, пол, предыдущий опыт в
# программировании (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по
# 10-балльной шкале. Необходимо написать программу, которая в зависимости от запроса пользователя будет выводить:
# среднюю оценку за домашние задания и за экзамен по всем группе в следующем виде:
#         Средняя оценка за домашние задания по группе: X
#         Средняя оценка за экзамен: Y
# где X и Y - вычисляемые значения;
# среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола
# б)наличия опыта в виде:
#         Средняя оценка за домашние задания у мужчин: A
#         Средняя оценка за экзамен у мужчин: B
#         Средняя оценка за домашние задания у женщин: C
#         Средняя оценка за экзамен у женщин: D
#         Средняя оценка за домашние задания у студентов с опытом: E
#         Средняя оценка за экзамен у студентов с опытом: F
#         Средняя оценка за домашние задания у студентов без опыта: G
#         Средняя оценка за экзамен у студентов без опыта: H
# где A, B, C, D, E, F, G, H - вычисляемые значения;
# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние
# задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение

students = [
    {'name': 'clark', 'surname': 'kent', 'sex': 'male', 'devexp': True, 'homework_marks': [3, 5, 8, 9, 10], 'exam': 8},
    {'name': 'james', 'surname': 'bond', 'sex': 'male', 'devexp': False, 'homework_marks': [3, 3, 4, 5, 7], 'exam': 6},
    {'name': 'john', 'surname': 'snow', 'sex': 'male', 'devexp': True, 'homework_marks': [8, 7, 8, 3, 7], 'exam': 6},
    {'name': 'scarlet', 'surname': 'ohara', 'sex': 'female', 'devexp': False, 'homework_marks': [2, 4, 5, 8, 9],
     'exam': 8},
    {'name': 'sarah', 'surname': 'connor', 'sex': 'female', 'devexp': True, 'homework_marks': [4, 4, 4, 6, 6],
     'exam': 7},
    {'name': 'indiana', 'surname': 'jones', 'sex': 'female', 'devexp': False, 'homework_marks': [7, 5, 5, 7, 10],
     'exam': 9},
    {'name': 'indiana', 'surname': 'jones', 'sex': 'male', 'devexp': True, 'homework_marks': [7, 5, 5, 7, 10],
     'exam': 9},
    {'name': 'bruce', 'surname': 'wayn', 'sex': 'male', 'devexp': False, 'homework_marks': [4, 3, 7, 10, 10],
     'exam': 5}]


def list_avg(a):  # функция вычисления среднего значения в списке (вспомогательная)
    sum_marks = 0
    for i, j in enumerate(a):
        sum_marks = sum_marks + a[i]
    avg = round(sum_marks / len(a), 2)
    return avg


def homework_average(a):  # функция вычисления средней оценки ГРУППЫ по ДЗ
    total_marks = []
    for k, v in enumerate(a):
        total_marks.extend(a[k]['homework_marks'])
    return list_avg(total_marks)


def exam_average(a):  # функция вычисления средней оценки ГРУППЫ по ЭКЗАМЕНУ
    total_marks = 0
    for k, v in enumerate(a):
        total_marks += a[k]['exam']
    exam_avg = round(total_marks / len(a), 2)
    return exam_avg


def homework_average_sex(a, b):  # функция вычисления средней оценки ПОЛА по ДЗ
    total_marks = []
    for k, v in enumerate(a):
        if a[k]['sex'] == b:
            total_marks.extend(a[k]['homework_marks'])
    return list_avg(total_marks)


def exam_average_sex(a, b):  # функция вычисления средней оценки ПОЛА по ЭКЗАМЕНУ
    total_marks = 0
    person_number = 0
    for k, v in enumerate(a):
        if a[k]['sex'] == b:
            total_marks += a[k]['exam']
            person_number += 1
    exam_avg = round(total_marks / person_number, 2)
    return exam_avg


def homework_average_exp(a, b):  # функция вычисления средней оценки c учетом опыта
    total_marks = []
    for k, v in enumerate(a):
        if a[k]['devexp'] == b:
            total_marks.extend(a[k]['homework_marks'])
    return list_avg(total_marks)


def exam_average_exp(a, b):  # функция вычисления средней оценки по ЭКЗАМЕНУ с учетом опыта
    total_marks = 0
    person_number = 0
    for k, v in enumerate(a):
        if a[k]['devexp'] == b:
            total_marks += a[k]['exam']
            person_number += 1
    exam_avg = round(total_marks / person_number, 2)
    return exam_avg


# def integral_marks(a): # функция определения лучших студентов
#   students_int_marks = {}
#   int_marks_list = []
#   for k, v in enumerate(a):
#     students_int_marks[a[k]['name'] + ' ' + a[k]['surname']] = 0.6 * list_avg(a[k]['homework_marks']) + 0.4 *
# a[k]['exam']
#     int_marks_list.append(0.6 * list_avg(a[k]['homework_marks']) + 0.4 * a[k]['exam'])
#   max_mark = max(int_marks_list)
#   print('Лучшие студенты:')
#   for k, v in students_int_marks.items():
#     if max_mark == v:
#       print('{0} с интегральной оценкой {1}'.format(k, v))
#   print(students_int_marks)
#   return students_int_marks

def integral_marks(a):  # функция определения лучших студентов
    students_names = []
    int_marks_list = []
    for k, v in enumerate(a):
        students_names.append(a[k]['name'] + ' ' + a[k]['surname'])
        int_marks_list.append(0.6 * list_avg(a[k]['homework_marks']) + 0.4 * a[k]['exam'])
    max_mark = max(int_marks_list)
    print('Лучшие студенты:')
    for i, k in enumerate(int_marks_list):
        if max_mark == k:
            print('{0} с интегральной оценкой {1}'.format(students_names[i], k))


print('Средняя оценка за домашние задания по группе:', homework_average(students))
print('Средняя оценка за экзамен по группе:', exam_average(students))
print('Средняя оценка за домашние задания у мужчин:', homework_average_sex(students, 'male'))
print('Средняя оценка за экзамен у мужчин:', exam_average_sex(students, 'male'))
print('Средняя оценка за домашние задания у женщин:', homework_average_sex(students, 'female'))
print('Средняя оценка за экзамен у женщин:', exam_average_sex(students, 'female'))
print('Средняя оценка за домашние задания у студентов с опытом:', homework_average_exp(students, True))
print('Средняя оценка за экзамен у студентов с опытом:', exam_average_exp(students, True))
print('Средняя оценка за экзамен у студентов без опыта:', exam_average_exp(students, False))
print('Средняя оценка за домашние задания у студентов без опыта:', homework_average_exp(students, False))

integral_marks(students)
