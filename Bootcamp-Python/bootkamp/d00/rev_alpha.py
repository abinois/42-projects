from sys import argv

print(" ".join([arg[::-1].swapcase() for arg in argv[:0:-1]]))