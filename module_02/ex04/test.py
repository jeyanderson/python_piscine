import my_minipack.progressbar as pg
from time import sleep

listy = range(50)
ret = 0
for elem in pg.ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.1)
print()
print(ret)