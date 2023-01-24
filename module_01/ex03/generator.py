from random import randint
from typing import Union
from sys import stderr


def generator(text: str, sep: str = ' ', option: Union[str, None] = None):
    '''
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings
    before it is yielded.
    '''
    if (
        not isinstance(text, str) or
        not isinstance(sep, str) or
        option is not None and option not in ['shuffle', 'unique', 'ordered']
    ):
        print("ERROR", file=stderr)
        return
    text = text.split(sep)
    if option == 'shuffle':
        for i in range(len(text)):
            j = randint(0, len(text) - 1)
            text[i], text[j] = text[j], text[i]
    elif option == 'unique':
        text = list(dict.fromkeys(text))
    elif option == 'ordered':
        text = sorted(text, key=lambda s: s.casefold())
    yield from text
