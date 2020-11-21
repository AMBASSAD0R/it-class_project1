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


def pa(mass_a, mass_b):
    if not mass_b:
        return None
    mass_a = ft_rev_list(mass_a)
    mass_a.append(mass_b[0])
    return ft_rev_list(mass_a)


def pb(mass_b, mass_a):
    if not mass_a:
        return None
    mass_b = ft_rev_list(mass_b)
    mass_b.append(mass_a[0])
    return ft_rev_list(mass_b)
