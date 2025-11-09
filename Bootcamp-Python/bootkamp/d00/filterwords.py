from sys import exit, argv
import re

if len(argv) != 3 or not argv[2].isdigit() or argv[1].isdigit():
    exit('ERROR')
print([ _ for _ in re.sub(r'[\s;,.?!`\"\']+', ' ', argv[1]).split(' ') if len(_) >= int(argv[2]) ])