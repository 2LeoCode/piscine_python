from functools import reduce

def what_are_the_vars(*args, **kwargs):
    result = ObjectC()
    list(setattr(result, f"var_{i}", x) for (x, i) in enumerate(args))
    result.__dict__.update(kwargs)
    return result


class ObjectC(object):
    def __init__(self):
        super()

    def __repr__(self):
        return (
            "ObjectC {\n"
            f"""{reduce(
                lambda x, y: x + y,
                map(
                    lambda x: f'{chr(9)}{x}: {getattr(self, x)},{chr(10)}',
                    (x for x in dir(self) if not x.startswith("__"))
                )
            )}""" + "}"
        )

    def __str__(self):
        return self.__repr__()



if __name__ == "__main__":
    obj = what_are_the_vars(1, 2, 3, kek=4, lol=5, lel=6)
    print(obj)
