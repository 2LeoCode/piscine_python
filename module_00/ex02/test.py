from subprocess import run, PIPE, DEVNULL
from sys import stderr


def test(args: 'list[str]', expected: str = ..., error: str = ...):
    res = run(["python", "whois.py"] + args, stdout=PIPE, stderr=PIPE)
    if error is ... and expected is ...:
        print(
            "[Error] No expected output or error message provided",
            file=stderr
        )
        return
    print(
        "[KO]" if
        error is not ... and res.stderr.decode() != error
        or expected is not ... and res.stdout.decode() != expected
        else "[OK]"
    )


test(["42"], expected="I'm even\n", error="")
test(["421"], expected="I'm odd\n", error="")
test(["-42"], expected="I'm even\n", error="")
test(["-421"], expected="I'm odd\n", error="")
test(["0"], expected="I'm zero\n", error="")
test(["-0"], expected="I'm zero\n", error="")
test([], expected="")
test(
    ["Hello"],
    expected="",
    error="AssertionError: argument is not an integer\n"
)
test(
    ["Hello", "42"],
    expected="",
    error="AssertionError: more than one argument are provided\n"
)
test(
    ["42", "42"],
    expected="",
    error="AssertionError: more than one argument are provided\n"
)
test(
    ["42", "42", "42"],
    expected="",
    error="AssertionError: more than one argument are provided\n"
)
