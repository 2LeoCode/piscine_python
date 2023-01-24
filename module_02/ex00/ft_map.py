def ft_map(function, iterable, *iterables):
    return (function(*x) for x in zip(*((iterable,) + iterables)))
