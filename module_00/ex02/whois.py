from sys import argv, stderr

if len(argv) == 1:
    print(f"usage: python {argv[0]} <0-9 string>", file=stderr)
elif len(argv) != 2:
    print("AssertionError: more than one argument are provided", file=stderr)
else:
    try:
        n = int(argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer", file=stderr)
    else:
        print("I'm odd" if n % 2 else "I'm even" if n else "I'm zero")
