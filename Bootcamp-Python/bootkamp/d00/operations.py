from sys import exit, argv as av

usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
if len(av) != 3:
    if len(av) > 3:
        print("InputError: too many arguments\n")
    exit(usage)
for a in av[1::]:
    if not a.isdigit():
        print("InputError: only numbers\n")
        exit(usage)
op = {
    "Sum:": lambda a, b: a + b,
    "Difference:": lambda a, b: a - b, 
    "Product:": lambda a, b: a * b,
    "Quotient:": lambda a, b: a / b if b else 'ERROR (div by zero)',
    "Remainder:": lambda a, b: a % b if b else 'ERROR (modulo by zero)'}

for ope, f in op.items():
    print("{}{}".format(ope.ljust(15), f(int(av[1]), int(av[2]))))