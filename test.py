# def ft_len(st):
#     kol = 0
#     for i in st:
#         kol += 1
#     return kol
#
#
# def sa(mass_a):
#     if ft_len(mass_a) > 1:
#         mass_a[0], mass_a[1] = mass_a[1], mass_a[0]
#         return mass_a
#
#
# def sb(mass_b):
#     if ft_len(mass_b) > 1:
#         mass_b[0], mass_b[1] = mass_b[1], mass_b[0]
#         return mass_b
#
#
# def ss(mass_a, mass_b):
#     return sa(mass_a), sb(mass_b)


# from rra_rrb_rrr import *
# from ra_rb_rr import *
#
#
# def ft_find_lst(mass, char):
#     for i in range(len(mass)):
#         if mass[i] == char:
#             return i
#
#
# mass_a = [5, 2, 3, 1, 4, -1, -4, 7, 6, 9]
# result = []
# i = 0
#
# while mass_a:
#
#     # индекс минимального элмента
#     minimal_index = ft_find_lst(mass_a, min(mass_a))
#
#     # если первый элемент - минимум, то убераем его в другой стэк и сортируем дальше
#     if min(mass_a) == mass_a[0]:
#         print('pb')
#         result.append(mass_a[0])
#         mass_a = mass_a[1:]
#     else:
#         # находим рассстояние от концов
#         # списка до концов списка и находим до куда ближе
#         if minimal_index >= len(mass_a) - minimal_index - 1:
#             mass_a = rra(mass_a)
#             print('rra')
#         elif minimal_index <= len(mass_a) - minimal_index - 1:
#             mass_a = ra(mass_a)
#             print('ra')
#     print(i, mass_a)
#     i += 1
#
# print(result)


# def console_output(command):
#     print('COMMAND' + '\033[31m', command, '\033[0m')
#     print(f'MASSIVE_A:')
#     print(f'MASSIVE_B:')
#     print('=' * 10)
#
#
# console_output('pb')

# from additional_function import ft_slice, ft_find_lst, ft_len
#
#
# def ft_split(string):
#     new_mass = []
#     while string:
#         space = ft_find_lst(string, ' ')
#         new_mass.append(string[:space + 1])
#         string = string[space + 1:]
#     return new_mass
#
#
# print(ft_split('123 32 421 12'))

a = ['12', '13123', '34123']
for i in range(len(a)):
    a[i] = int(a[i])
print(a)