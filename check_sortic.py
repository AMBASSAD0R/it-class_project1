from pa_pb import *
from ra_rb_rr import *
from sa_sb_ss import *
from rra_rrb_rrr import *

mass_a_numbers = mass_b_numbers = []

mass_a_commands = mass_b_commands = []

number = input()
while number != '!':
    mass_a_numbers.append(int(number))
    number = input()

command = input()
while command != '*':
    mass_a_commands.append(command)
    command = input()

while mass_a_numbers:
    for command in mass_a_commands:
        if command == sa(mass_a_numbers)[-1]:
            mass_a_numbers = sa(mass_a_numbers)

        elif command == ra(mass_a_numbers)[-1]:
            mass_a_numbers = ra(mass_a_numbers)

        elif command == pa(mass_a_numbers, mass_b_numbers)[-1]:
            mass_a_numbers = rra(mass_a_numbers)

        elif command == rra(mass_a_numbers)[-1]:
            mass_a_numbers = sa(mass_a_numbers)

        elif command == ss(mass_a_numbers, mass_b_numbers)[-1]:
            mass_a_numbers = ss(mass_a_numbers, mass_b_numbers)

        elif command == rrr(mass_a_numbers, mass_b_numbers)[-1]:
            mass_a_numbers = rrr(mass_a_numbers, mass_b_numbers)

        else:
            pass

print(mass_a_numbers)
