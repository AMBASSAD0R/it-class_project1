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
