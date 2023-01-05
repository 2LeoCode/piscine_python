from sys import argv, stderr

if len(argv) == 1:
    print("usage: python operations.py <number1> <number2>", file=stderr)
elif len(argv) == 2:
    print("AssertionError: not enough arguments", file=stderr)
elif len(argv) > 3:
    print("AssertionError: too many arguments", file=stderr)
else:
    try:
        a = int(argv[1])
        b = int(argv[2])
    except ValueError:
        print("AssertionError: only integers", file=stderr)
    else:
        print(
            f"Sum: {a + b}\n"
            f"Difference: {a - b}\n"
            f"Product: {a * b}\n"
            f"Quotient: {a / b if b != 0 else 'ERROR (division by zero)'}\n"
            f"Remainder: {a % b if b != 0 else 'ERROR (modulo by zero)'}"
        )
