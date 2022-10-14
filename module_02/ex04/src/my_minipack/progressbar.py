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
        eta=00.00if ih/10<1 else eta
        sys.stdout.write('\r')
        sys.stdout.write(f"ETA: {eta:5}s [{round(ih/toolbar_width * 100,2):5}] [{'='*int(ih/2):50}] {ih:3}/{toolbar_width}  |  elapsed time {round(time.time()-start,2):5}s")
        sys.stdout.flush()
        yield i