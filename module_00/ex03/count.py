from sys import argv, stderr
from string import punctuation


def text_analyzer(txt: str = ...):
    """
    This function counts the number of character from a given text.
    It also counts the number of upper case characters, lower case characters,
    punctuation and spaces inside that text.\n

    Keyword arguments:\n
    txt -- an optional argument of type str, if not provided or None, the
    function will ask the user to input a text.
    """

    if txt == ... or txt == None:
        print("What is the text to analyse?")
        txt = input()
    if not isinstance(txt, str):
        raise TypeError("AssertionError: argument is not a string")
    print(
        f"The text contains {len(txt)} character(s):\n"
        f"{sum(c.isupper() for c in txt)} upper letter(s)\n"
        f"{sum(c.islower() for c in txt)} lower letter(s)\n"
        f"{sum(txt.count(c) for c in punctuation)} punctuation mark(s)\n"
        f"{sum(c.isspace() for c in txt)} space(s)"
    )


if __name__ == "__main__":
    if len(argv) <= 2:
        text_analyzer(argv[1] if len(argv) == 2 else None)
    else:
        print(
            "AssertionError: more than one argument are provided",
            file=stderr
        )
