def ft_reduce(func,iterable):
    try:
        iter(iterable)
    except Exception:
        raise TypeError('ft_reduce() arg 2 must support iteration')
    if not iterable:
        raise TypeError('ft_reduce() of empty sequence')
    for i,item in enumerate(iterable):
        if i:
            try:
                result=func(result,item)
            except Exception:
                raise ValueError('error while executing provided function.')
        else: result=item
    return result

def cool(integer):
    return integer*2

ituple=['H','e','l']
print(ft_reduce(lambda u,v:u+v,ituple))