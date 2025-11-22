import sys

try:
    name = sys.argv[1]
    print("Hello,", name)
except IndexError:
    print("No name given! Please add one argument.")