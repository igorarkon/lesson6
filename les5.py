# Урок 5
# Задание 1: Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_obj = open("test.txt", "w")
lin = input("Введите текст: ")
while lin:
    f_obj.write(lin + '\n')
    lin = input("Введите текст: ")
    if not lin:
        break

f_obj.close()

#  Задание 2: Создать текстовый файл (не программно), сохранить в нем несколько строк,
#  выполнить подсчет количества строк, количества слов в каждой строке.

f = open('python.txt')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
f.close()

# Задание 3:
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников.

with open('rabota.txt', 'r', encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')

# Задание 4: Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('les5-4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with open('les5-4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# Задание 5: Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def task_five():
    try:
        with open('test.txt', 'w+') as file_obj:
            line = input('Введите цифры: \n')
            file_obj.writelines(line)
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Неправельно набрано')

    my_numb = line.split()
    print(sum(map(int, my_numb)))

task_five()

# Задание 6: Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

file = open("les6.txt")
a = (file.readline())
b = ''
while a:
    b = b + a
    a = file.readline()
b = b.split(' ')
result = 0
for i in b:
    if(i.isdigit()):
        result = result + int(i)
print(result)