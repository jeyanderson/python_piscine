def ft_filter(func,iterable):
    if not callable(func):
        raise ValueError('first argument need to be a function.')
    try:
        iter(iterable)
    except Exception:
        raise TypeError('ft_reduce() arg 2 must support iteration')
    try:
        for item in iterable:
            if func(item):
                yield(item)
    except:
        raise ValueError('error while executing the provided function.')

def cool(integer):
    return integer*2

ituple=[1,2,3]
print(list(ft_filter(lambda x: not (x%2),ituple)))