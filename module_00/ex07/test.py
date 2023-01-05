from subprocess import run, PIPE
from sys import stderr


def test(args: 'list[str]', expected: str = ..., error: str = ...):
    if error is ... and expected is ...:
        print(
            "[Error] No expected output or error message provided",
            file=stderr
        )
        return
    res = run(["python", "filterwords.py"] + args, stdout=PIPE, stderr=PIPE)
    print(
        "[KO]" if
        error is not ... and res.stderr.decode() != error
        or expected is not ... and res.stdout.decode() != expected
        else "[OK]"
    )


test(
    ["Hello, my friend !", "3"],
    expected="['Hello', 'friend']\n",
    error=""
)

test(
    ["Hello, my fri.....end !", "0"],
    expected="['Hello', 'my', 'friend']\n",
    error=""
)

test(
    ["Hello --^w**%';;o..?r)!&(l-=++d;+;;", "-1"],
    expected="['Hello', 'world']\n",
    error=""
)

test(
    ["Hello, my friend !", "a"],
    expected="",
    error="ERROR\n"
)

test(
    ["Hello, my friend !", "3", "4"],
    expected="",
    error="ERROR\n"
)

test(
    ["Hello, my friend !"],
    expected="",
    error="ERROR\n"
)
