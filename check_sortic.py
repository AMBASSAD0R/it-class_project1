from sotric_func import sortic

mass_a_numbers = []
mass_a_commands = []

number = input()
while number != '!':
    mass_a_numbers.append(int(number))
    number = input()

command = input()
while command != '*':
    mass_a_commands.append(command)
    command = input()

if mass_a_commands == sortic(mass_a_numbers):
    print('OK')
else:
    print('KO')
