from additional_function import *
from rra_rrb_rrr import *
from ra_rb_rr import *
from pa_pb import *
from sys import argv

mass_a = []
mass_b = []


# проверка корректности введенного значения

def is_number(number):
    wrong_symbols = list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
                         'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю'
                         '!"№;%:?*()_+~!@#$%^&*()_+{}:"><?/.,][|/')
    for i in number:
        if i in wrong_symbols or (number[0] == '0' and ft_len(number) > 1):
            return False
    return True


def ft_split(string):
    tmp = ''
    mass = []
    for ch in string:
        if ch == ' ' and tmp:
            mass.append(int(tmp))
            tmp = ''
        else:
            tmp += ch
    if tmp:
        mass.append(int(tmp))
    return mass


# функция, которая выводит визуализацию процесса сортировки в output.txt


def txt_output(fname, command):
    fname.write(f'COMMAND {command}' + '\n')
    fname.write(f'MASSIVE_A: {mass_a}' + '\n')
    fname.write(f'MASSIVE_B: {mass_b}' + '\n')
    fname.write('=' * ft_len(f'MASSIVE_B: {mass_b}') + '\n')


# функция, которая выводит визуализацию процесса сортировки в консоль

def console_output(command):
    print('COMMAND' + '\033[31m', command, '\033[0m')
    print(f'MASSIVE_A: {mass_a}')
    print(f'MASSIVE_B: {mass_b}')
    print('=' * ft_len(f'MASSIVE_B: {mass_b}'))


file = open('input.txt', mode='r', encoding='UTF-8')

lines = file.readlines()  # читаем файл
lines = [ft_split(line) for line in lines]  # распарсили данные из файла; example: ['123 321'] -> ['123', '321']

if ft_len(lines) > 0:
    for line in lines:
        for number in line:
            mass_a.append(int(number))
elif ft_len(argv) > 1:
    mass_a = ft_slice(argv, 1, ft_len(argv))
    for i in range(ft_len(mass_a)):
        mass_a[i] = int(mass_a[i])
else:
    numbers = input()
    if ' ' in numbers:
        numbers = ft_split(numbers)
        for i in range(0, ft_len(numbers)):
            mass_a.append(int(numbers[i]))
    else:
        while numbers != '!':
            if is_number(numbers):
                mass_a.append(int(numbers))
                numbers = input()
            else:
                print('Вы ввели несуществующее число!!!')
                print('Введите другое')
                numbers = input()

file.close()

iterator = 1

file2 = open('output.txt', mode='w')

while mass_a:
    file2.write(f'Iteration: {iterator}' + '\n')
    print(f'Iteration: {iterator}')

    pb(mass_b, mass_a)
    mass_a = ft_slice(mass_a, 1, ft_len(mass_a))
    console_output('pb')
    txt_output(file2, 'pb')

    iterator += 1


print(mass_b)

while mass_b:

    # индекс минимального элмента
    minimal_index = ft_find_lst(mass_b, ft_min(mass_b))
    file2.write(f'Iteration: {iterator}' + '\n')
    print(f'Iteration: {iterator}')

    # если первый элемент - минимум, то убераем его в другой стэк и сортируем дальше
    if ft_min(mass_b) == mass_b[0]:
        txt_output(file2, 'pa')
        mass_a.append(mass_b[0])
        mass_b = ft_slice(mass_b, 1, ft_len(mass_b))
        console_output('pa')
    else:
        # находим рассстояние от концов
        # списка до концов списка и находим до куда ближе
        if minimal_index >= ft_len(mass_b) - minimal_index - 1:
            mass_b = rrb(mass_b)
            txt_output(file2, 'rrb')
            console_output('rrb')
        elif minimal_index <= ft_len(mass_b) - minimal_index - 1:
            mass_b = rb(mass_b)
            txt_output(file2, 'rb')
            console_output('rb')

    iterator += 1

file2.close()
