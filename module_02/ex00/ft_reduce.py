def ft_reduce(function, iterable, initializer=None):
    iterable = iter(iterable)
    result = next(iterable, None) if initializer is None else initializer
    for x in iterable:
        result = function(result, x)
    return result
