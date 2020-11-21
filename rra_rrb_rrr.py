from additional_function import ft_rev_list, ft_len


def rra(mass_a):
    new_mass = list()
    ft_rev_list(mass_a).append(mass_a[0])
    for i in range(ft_len(ft_rev_list(mass_a)) - 1):
        new_mass.append(mass_a[i])
    return new_mass


def rrb(mass_b):
    new_mass = list()
    ft_rev_list(mass_b).append(mass_b[0])
    for i in range(ft_len(ft_rev_list(mass_b)) - 1):
        new_mass.append(mass_b[i])
    return new_mass


def rrr(mass_a, mass_b):
    return rra(mass_a), rrb(mass_b)


print(rrb([1, 2, 3, 4]))