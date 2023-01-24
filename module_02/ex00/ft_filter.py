def ft_filter(function, iterable):
    return (x for x in iterable if function(x))
