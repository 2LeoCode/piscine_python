from subprocess import run, PIPE
from sys import stderr


def test(args: 'list[str]', expected: str = ..., error: str = ...):
    if error is ... and expected is ...:
        print(
            "[Error] No expected output or error message provided",
            file=stderr
        )
        return
    res = run(["python", "operations.py"] + args, stdout=PIPE, stderr=PIPE)
    print(
        "[KO]" if
        error is not ... and res.stderr.decode() != error
        or expected is not ... and res.stdout.decode() != expected
        else "[OK]"
    )


test(
    ["1", "2"],
    expected=(
        "Sum: 3\n"
        "Difference: -1\n"
        "Product: 2\n"
        "Quotient: 0.5\n"
        "Remainder: 1\n"
    ),
    error=""
)

test(
    ["1", "2", "3"],
    expected="",
    error="AssertionError: too many arguments\n"
)

test(
    ["1"],
    expected="",
    error="AssertionError: not enough arguments\n"
)

test(
    ["1", "a"],
    expected="",
    error="AssertionError: only integers\n"
)

test(
    ["a", "1"],
    expected="",
    error="AssertionError: only integers\n"
)

test(
    ["1", "0"],
    expected=(
        "Sum: 1\n"
        "Difference: 1\n"
        "Product: 0\n"
        "Quotient: ERROR (division by zero)\n"
        "Remainder: ERROR (modulo by zero)\n"
    ),
    error=""
)

test(
    [],
    expected=""
)

test(
    ["1", "2", "3", "4"],
    expected="",
    error="AssertionError: too many arguments\n"
)

test(
    ["1"],
    expected="",
    error="AssertionError: not enough arguments\n"
)

test(
    ["a", "b", "c"],
    expected="",
    error="AssertionError: too many arguments\n"
)

test(
    ["a"],
    expected="",
    error="AssertionError: not enough arguments\n"
)

test(
    ["-1", "2"],
    expected=(
        "Sum: 1\n"
        "Difference: -3\n"
        "Product: -2\n"
        "Quotient: -0.5\n"
        "Remainder: 1\n"
    ),
    error=""
)

test(
    ["1", "-2"],
    expected=(
        "Sum: -1\n"
        "Difference: 3\n"
        "Product: -2\n"
        "Quotient: -0.5\n"
        "Remainder: -1\n"
    ),
    error=""
)
