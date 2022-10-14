import time
import os

def log(func):
    def inner(*args,**kwargs):
        start=time.time()
        ret=func(*args,**kwargs)
        end=time.time()
        delta=end-start
        exec_time=f"{delta if delta>=1 else delta*1000:.3f} {'s'if delta>=1 else 'ms'}"
        string=f"({os.environ['USER']})Running: {func.__name__.replace('_',' ').title():20}[ exec-time = {exec_time} ]"
        with open('machine.log','a')as file:
            file.write(string+'\n')
        return ret
    return inner