from sys import argv, stderr

if len(argv) == 1:
    print(
        f"usage: python {argv[0]} <a-zA-Z string> [a-zA-Z string...]",
        file=stderr
    )
else:
    print(" ".join(argv[1:])[::-1].swapcase())
