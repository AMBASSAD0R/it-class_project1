from rra_rrb_rrr import *
from ra_rb_rr import *
from additional_function import ft_find_lst

mass_a = mass_b = []

number = input()
while number != '!':
    mass_a.append(int(number))
    number = input()

print(mass_a)

i = 0

while mass_a:

    # индекс минимального элмента
    minimal_index = ft_find_lst(mass_a, min(mass_a))

    # если первый элемент - минимум, то убераем его в другой стэк и сортируем дальше
    if min(mass_a) == mass_a[0]:
        print('pb')
        mass_b.append(mass_a[0])
        mass_a = mass_a[1:]
    else:
        # находим рассстояние от концов
        # списка до концов списка и находим до куда ближе
        if minimal_index >= len(mass_a) - minimal_index - 1:
            mass_a = rra(mass_a)
            print('rra')
        elif minimal_index <= len(mass_a) - minimal_index - 1:
            mass_a = ra(mass_a)
            print('ra')
    # print(i, mass_a)
    i += 1

mass_a = mass_b

print(mass_b)
