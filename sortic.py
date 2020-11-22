from rra_rrb_rrr import *
from ra_rb_rr import *
from additional_function import ft_find_lst, ft_len, ft_min, ft_slice

mass_a = []
mass_b = []

file = open('input.txt', mode='r', encoding='UTF-8')
lines = file.readlines()
for line in lines:
    for char in line:
        if char != ' ':
            mass_a.append(int(char))

iterator = 1

while mass_a:

    # индекс минимального элмента
    minimal_index = ft_find_lst(mass_a, ft_min(mass_a))
    print(f'Iteration: {iterator}')

    # если первый элемент - минимум, то убераем его в другой стэк и сортируем дальше
    if ft_min(mass_a) == mass_a[0]:
        print("COMMAND" + "\033[31m {}" .format("pb") + "\033[0m")
        mass_b.append(mass_a[0])
        mass_a = ft_slice(mass_a, 1, ft_len(mass_a))
        print(f'MASSIVE_A: {mass_a}')
        print(f'MASSIVE_B: {mass_b}')
        print('=' * ft_len(f'MASSIVE_B: {mass_b}'))
    else:
        # находим рассстояние от концов
        # списка до концов списка и находим до куда ближе
        if minimal_index >= ft_len(mass_a) - minimal_index - 1:
            mass_a = rra(mass_a)
            print("COMMAND" + "\033[31m {}".format("rra") + "\033[0m")
            print(f'MASSIVE_A: {mass_a}')
            print(f'MASSIVE_B: {mass_b}')
            print('=' * ft_len(f'MASSIVE_B: {mass_b}'))
        elif minimal_index <= ft_len(mass_a) - minimal_index - 1:
            mass_a = ra(mass_a)
            print("COMMAND" + "\033[31m {}" .format("ra") + "\033[0m")
            print(f'MASSIVE_A: {mass_a}')
            print(f'MASSIVE_B: {mass_b}')
            print('=' * ft_len(f'MASSIVE_B: {mass_b}'))

    iterator += 1

mass_a = mass_b

result_string = ''
for number in mass_a:
    result_string += str(number) + ' '


file = open('output.txt', mode='w')
file.write(result_string)
file.close()