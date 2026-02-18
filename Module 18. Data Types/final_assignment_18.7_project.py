import random
# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students: # 1 итерация: student = 'Александра'
    students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes: # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student} {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку 
        5. Редактировать оценку
        6. Вывод информации по всем оценкам для определенного ученика
        7. Вывод среднего балла по каждому предмету по определенному ученику
        8. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].pop(mark)
            print(f'Для {student} по предмету {class_} удалена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('5. Редактировать оценку')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            new_mark = input('Введите новую оценку: ')
            students_marks[student][class_].pop(mark)
            students_marks[student][class_].append(new_mark)
            print(f'Для {student} по предмету {class_} добавлена новая оценка {new_mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 6:
        print('6. Вывод информации по всем оценкам для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 7:
        print('7. Вывод среднего балла по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
               marks_sum = sum(students_marks[student][class_])
               marks_count = len(students_marks[student][class_])
               print(f'{class_} - {marks_sum // marks_count}')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 8:
        print('8. Выход из программы')
        break
