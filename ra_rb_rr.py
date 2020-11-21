from additional_function import ft_len


def ra(mass_a):
    """
    сдвиг всех элементов стека а на 1 вверх. Первый элемент становится последним
    """
    x = mass_a[0]
    mass_cop = []
    for i in range(1, ft_len(mass_a)):
        mass_cop.append(mass_a[i])
    mass_cop.append(x)
    return mass_cop


def rb(mass_b):
    """
    сдвиг всех элементов стека b на 1 вверх. Первый элемент становится последним
    """
    x = mass_b[0]
    mass_cop = []
    for i in range(1, ft_len(mass_b)):
        mass_cop.append(mass_b[i])
    mass_cop.append(x)
    return mass_cop


def rr(mass_a, mass_b):
    """ra и rb одновременно"""
    return ra(mass_a), rb(mass_b)
