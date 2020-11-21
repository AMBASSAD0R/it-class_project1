from rra_rrb_rrr import *
from ra_rb_rr import *


def ft_find_lst(mass, char):
    for i in range(len(mass)):
        if mass[i] == char:
            return i


mass_a = [5, 2, 3, 1, 4, -1, -4, 7, 6, 9]
result = []
i = 0

while mass_a:

    # индекс минимального элмента
    minimal_index = ft_find_lst(mass_a, min(mass_a))

    # если первый элемент - минимум, то убераем его в другой стэк и сортируем дальше
    if min(mass_a) == mass_a[0]:
        print('pb')
        result.append(mass_a[0])
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
    print(i, mass_a)
    i += 1

print(result)