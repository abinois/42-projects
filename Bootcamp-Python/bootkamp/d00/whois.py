from sys import argv

if len(argv) == 2 and argv[1].isdigit():
    print("I'm Even." if not int(argv[1]) % 2 else "I'm Odd.")
else:
    print('ERROR')