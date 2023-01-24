from itertools import chain
from typing import Union, List, Tuple
from sys import stderr


class Vector:
    def __init__(self, init: Union[
                               int,
                               Tuple[int, int],
                               List[List[Union[int, float]]]
                             ]):
        if isinstance(init, int):
            size = init
            self.shape = (1, size)
            self.values = [[x] for x in range(size)]
        elif isinstance(init, tuple):
            a, b = init
            if a > b:
                print("Warning: range is negative.", file=stderr)
            rg = range(a, b) if a < b else reversed(range(b, a))
            self.shape = (1, max(a, b) - min(a, b))
            self.values = [[x] for x in rg]
        elif isinstance(init, list):
            assert (
                len(init) == 1 or
                all(len(x) == 1 for x in init)
            ), "Vector must be a row or a column"
            size = len(init[0]) if len(init) == 1 else len(init)
            self.shape = (1, size) if len(init) == 1 else (size, 1)
            self.values = init
        else:
            raise AssertionError("Invalid initializer type")

    def dot(self, other: 'Vector'):
        assert isinstance(other, Vector), "other must be a Vector"
        assert self.shape == other.shape, "vectors must have the same shape"
        return sum([x[0] * x[1] for x in zip(
            chain(*self.values), chain(*other.values)
        )])

    def T(self):
        init = list(chain(*self.values))
        return Vector([init] if self.shape[0] == 1 else [[x] for x in init])

    def __add__(self, other: 'Vector'):
        assert isinstance(other, Vector), "other must be a Vector"
        assert self.shape == other.shape, "vectors must have the same shape"
        return Vector([[x] for x in map(
            lambda x: x[0] + x[1],
            zip(chain(*self.values), chain(*other.values))
        )])

    def __sub__(self, other: 'Vector'):
        assert isinstance(other, Vector), "other must be a Vector"
        assert self.shape == other.shape, "vectors must have the same shape"
        return Vector([[x] for x in map(
            lambda x: x[0] - x[1],
            zip(chain(*self.values), chain(*other.values))
        )])

    def __rsub__(self, other: 'Vector'):
        assert isinstance(other, Vector), "other must be a Vector"
        return other.__sub__(self)

    def __mul__(self, other: Union[int, float]):
        assert isinstance(other, (int, float)), "other must be a number"
        if self.shape[0] == 1:
            return Vector(
                [list(map(lambda x: x * other, chain(*self.values)))]
            )
        return Vector(
            list(map(lambda x: [x * other], chain(*self.values)))
        )

    def __rmul__(self, other: Union[int, float]):
        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float]):
        assert isinstance(other, (int, float)), "other must be a number"
        if other == 0:
            print("ZeroDivisionError: division by zero.", file=stderr)
        else:
            return Vector(
                [list(map(lambda x: x / other, chain(*self.values)))]
                if self.shape[0] == 1 else
                list(map(lambda x: [x / other], chain(*self.values)))
            )

    def __rtruediv__(self, other: Union[int, float]):
        print(
            "ArithmeticError: Division of a scalar by a Vector"
            " is not defined here.", file=stderr
        )

    def __repr__(self):
        return f"Vector({self.values})"

    def __str__(self):
        return self.__repr__()
