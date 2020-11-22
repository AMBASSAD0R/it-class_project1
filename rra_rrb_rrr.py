from additional_function import ft_len


def rra(mass_a):
    """сдвиг всех элементов стека a на 1 вниз"""
    res = [0] + mass_a
    res[0] = res[-1]
    res_x = []
    for i in range(ft_len(res) - 1):
        res_x.append(res[i])
    return res_x, "rra"


def rrb(mass_b):
    """ сдвиг всех элементов стека b на 1 вниз"""
    res = [0] + mass_b
    res[0] = res[-1]
    res_x = []
    for i in range(ft_len(res) - 1):
        res_x.append(res[i])
    return res_x, "rrb"


def rrr(mass_a, mass_b):
    """одновременно выполнить rra и rrb"""
    return rra(mass_a), rrb(mass_b), "rrr"
