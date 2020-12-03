from additional_function import *
from pa_pb import *
from ra_rb_rr import *
from rra_rrb_rrr import *
from sa_sb_ss import *

mass_a_numbers = []
mass_b_numbers = []
mass_commands = []

number = input()
while number != '!':
    mass_a_numbers.append(int(number))
    number = input()

command = input()
while command != '*':
    mass_commands.append(command)
    command = input()


def sorted_massive(mass):
    for i in range(1, ft_len(mass)):
        if mass[i] < mass[i - 1]:
            return 'KO'
    return 'OK'


for command in mass_commands:
    if command == 'pb':
        mass_b_numbers = pb(mass_b_numbers, mass_a_numbers)
        mass_a_numbers = ft_slice(mass_a_numbers, 1, ft_len(mass_a_numbers))
    elif command == 'pa':
        mass_a_numbers = pa(mass_a_numbers, mass_b_numbers)
        mass_b_numbers = ft_slice(mass_b_numbers, 1, ft_len(mass_b_numbers))
    elif command == 'ra':
        mass_a_numbers = ra(mass_a_numbers)
    elif command == 'rb':
        mass_b_numbers = rb(mass_b_numbers)
    elif command == 'rr':
        rr(mass_a_numbers, mass_b_numbers)
    elif command == 'sa':
        mass_a_numbers = sa(mass_a_numbers)
    elif command == 'sb':
        mass_b_numbers = sb(mass_b_numbers)
    elif command == 'ss':
        ss(mass_a_numbers, mass_b_numbers)
    elif command == 'rra':
        mass_a_numbers = rra(mass_a_numbers)
    elif command == 'rrb':
        mass_b_numbers = rrb(mass_b_numbers)
    elif command == 'rrr':
        rrr(mass_a_numbers, mass_b_numbers)

print(sorted_massive(mass_a_numbers))
