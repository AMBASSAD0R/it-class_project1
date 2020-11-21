def ft_len(mass):
    count = 0
    for _ in mass:
        count += 1
    return count


def ft_rev_list(mass):
    long = ft_len(mass)
    for i in range(ft_len(mass) // 2):
        x = mass[0 + i]
        u = mass[long - i - 1]
        mass[0 + i] = u
        mass[long - i - 1] = x
    return mass


def ft_min(mass):
    minimal = mass[0]
    for number in mass:
        if number < minimal:
            minimal = number
    return minimal


def ft_find_lst(mass, char):
    for i in range(len(mass)):
        if mass[i] == char:
            return i
