from subprocess import run, PIPE
from sys import stderr
from functools import partial


def test(
    args: 'list[str]', standalone: bool = False,
    expected: str = ..., error: str = ...
):
    if error is ... and expected is ...:
        print(
            "[Error] No expected output or error message provided",
            file=stderr
        )
        return
    run_pipe = partial(run, stdout=PIPE, stderr=PIPE)
    res = (
        run_pipe(["python", "count.py"] + args) if standalone
        else run_pipe([
            "python", "-c",
            f"from count import text_analyzer; text_analyzer(\"{args[0]}\")"
        ])
    )
    print(
        "[KO]" if
        error is not ... and res.stderr.decode() != error
        or expected is not ... and res.stdout.decode() != expected
        else "[OK]"
    )


test(["Hello, world !"], standalone=True,
    expected=(
        "The text contains 14 character(s):\n"
        "1 upper letter(s)\n"
        "9 lower letter(s)\n"
        "2 punctuation mark(s)\n"
        "2 space(s)\n"
    )
)
test(
    ["Hello, world !", "Hello, world !"], standalone=True,
    expected="",
    error="AssertionError: more than one argument are provided\n"
)

test(
    ["Hello, world !"],
    expected=(
        "The text contains 14 character(s):\n"
        "1 upper letter(s)\n"
        "9 lower letter(s)\n"
        "2 punctuation mark(s)\n"
        "2 space(s)\n"
    )
)