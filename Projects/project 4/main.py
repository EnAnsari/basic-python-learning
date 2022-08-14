# part 53 from 97
# project 4
# Module Project

import pyfiglet
# print(pyfiglet.figlet_format('python'))

from termcolor2 import colored

validColors = ('red', 'green', 'blue', 'cyan', 'yellow', 'magenta')

def print_art(color, message):
    if color not in validColors:
        color = 'red'
    ascii_art = pyfiglet.figlet_format(message)
    ascii_art = colored(ascii_art, color=color)
    print(ascii_art)

message = input('what would you like to print? ')
color = input('what color? ')
print_art(color, message)