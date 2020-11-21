from additional_function import ft_rev_list


def pa(mass_a, mass_b):
    """взять первый элемент в верхней части b и поместите его в верхнюю часть a."""
    if not mass_b:
        return None
    mass_a = ft_rev_list(mass_a)
    mass_a.append(mass_b[0])
    return ft_rev_list(mass_a)


def pb(mass_b, mass_a):
    """взять первый элемент в верхней части a и поместите его в верхнюю часть b"""
    if not mass_a:
        return None
    mass_b = ft_rev_list(mass_b)
    mass_b.append(mass_a[0])
    return ft_rev_list(mass_b)
