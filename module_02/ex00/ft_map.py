def ft_map(func,iterable):
    if not callable(func):
        raise ValueError('first argument need to be a function.')
    print(func)
    try:
        iter(iterable)
    except Exception:
        raise TypeError('ft_reduce() arg 2 must support iteration')
    try:
        for item in iterable:
            yield(func(item))
    except:
        raise ValueError('error while executing the provided function.')

def cool(integer):
    return integer*2

ituple=[1,2,3]
print(ft_map(lambda x: x+2,ituple))