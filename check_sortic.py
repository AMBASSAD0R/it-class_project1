from pa_pb import *
from ra_rb_rr import *
from sa_sb_ss import *
from rra_rrb_rrr import *
from additional_function import ft_len

mass_a_numbers = mass_b_numbers = []

mass_a_commands = mass_b_commands = []

number = input()
while number != '!':
    mass_a_numbers.append(int(number))
    number = input()

command = input()
while command != '*':
    command = input()
    mass_a_commands.append(command)
