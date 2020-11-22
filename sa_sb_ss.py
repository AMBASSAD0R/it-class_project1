from additional_function import ft_len


def sa(mass_a):
    """Меняет местами первые 2 элемента на вершине стека a"""
    if ft_len(mass_a) > 1:
        mass_a[0], mass_a[1] = mass_a[1], mass_a[0]
        return mass_a, "sa"


def sb(mass_b):
    """Меняет местами первые 2 элемента на вершине стека b"""
    if ft_len(mass_b) > 1:
        mass_b[0], mass_b[1] = mass_b[1], mass_b[0]
        return mass_b, "sb"


def ss(mass_a, mass_b):
    """sa и sb одновременно"""
    return sa(mass_a), sb(mass_b), "ss"
