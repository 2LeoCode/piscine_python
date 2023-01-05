from subprocess import run, PIPE
from sys import stderr


def test(args: 'list[str]', expected: str = ..., error: str = ...):
    if error is ... and expected is ...:
        print(
            "[Error] No expected output or error message provided",
            file=stderr
        )
        return
    res = run(["python", "sos.py"] + args, stdout=PIPE, stderr=PIPE)
    print(
        "[KO]" if
        error is not ... and res.stderr.decode() != error
        or expected is not ... and res.stdout.decode() != expected
        else "[OK]"
    )


test(
    ["sos"],
    expected="... --- ...\n",
    error=""
)

test(
    ["sos", "sos"],
    expected="... --- ... / ... --- ...\n",
    error=""
)

test(
    ["HELLO / WORLD"],
    expected="",
    error="ERROR\n"
)

test(
    ["96 BOULEVARD", "Bessiere"],
    expected=(
        "----. -.... / -... --- ..- .-.. . ...- "
        ".- .-. -.. / -... . ... ... .. . .-. .\n"
    ),
    error=""
)
