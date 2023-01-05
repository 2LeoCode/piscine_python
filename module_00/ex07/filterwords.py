from string import punctuation
from sys import argv, stderr

if len(argv) != 3:
    print("ERROR", file=stderr)
    exit()

try:
    n = int(argv[2])
except ValueError:
    print("ERROR", file=stderr)
else:
    print([
        word for word in argv[1].translate(
            str.maketrans('', '', punctuation)
        ).split() if len(word) > n
    ])
