from time import sleep
import time
import sys

def ft_progress(lst):
    toolbar_width=100
    start=time.time()
    eta=0
    for i in lst:
        ih=i/(len(lst)-1)*100
        ih=int(ih)
        if ih/10==1:
            eta=time.time()-start
            eta=round(eta*10,2)
        eta="TBD"if ih/10<1 else eta
        sys.stdout.write('\r')
        sys.stdout.write(f"ETA: {eta}s [%d%%] [%-{toolbar_width}s] %d/%d  |  elapsed time %.2fs" %
         ((ih/toolbar_width * 100),'='*ih,ih,toolbar_width,(time.time()-start)))
        sys.stdout.flush()
        yield i

listy = range(50)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.2)
print()
print(ret)