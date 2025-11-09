from sys import exit, argv
import re

MORSE_CODE_DICT = { 
    'A':'.-', 'B':'-...', 'C':'-.-.',
    'D':'-..', 'E':'.', 'F':'..-.',
    'G':'--.', 'H':'....', 'I':'..',
    'J':'.---', 'K':'-.-', 'L':'.-..',
    'M':'--', 'N':'-.', 'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.',
    'S':'...', 'T':'-', 'U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-',
    'Y':'-.--', 'Z':'--..', '1':'.----',
    '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...',
    '8':'---..', '9':'----.', '0':'-----'}
if len(argv) == 1:
    exit()
argz = []
for arg in argv[1::]:
    argz.extend(re.sub(r'\s', ' ', arg).split(' '))

for arg in argz:
    if not arg.isalnum():
        exit('ERROR')

for i, arg  in enumerate(argz):
    if i > 0:
        print('/ ', end='')
    for ltr in arg.upper():
        print(MORSE_CODE_DICT[ltr], end=' ')
print('')
    