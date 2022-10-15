from math import sqrt
from os import stat
from turtle import st

class TinyStatistician():
    @staticmethod
    def mean(x):
        if not len(x):
            return None
        try:
            return float(sum(x)/len(x))
        except Exception:
            raise TypeError('x should be a non-empty int/float list or array.')

    @staticmethod
    def median(x):
        if not len(x):
            return None
        try:
            x.sort()
            return float(x[len(x)//2]) if len(x)%2!=0 else float((x[len(x)//2]+x[len(x)//2-1])/2)
        except Exception:
            raise TypeError('x should be a non-empty int/float list or array.')
    @staticmethod
    def quartile(x):
        if not len(x):
            return None
        try:
            x.sort()
            q1list = []
            q2list = []
            for i in x:
                if i<TinyStatistician.median(x):
                    q1list.append(i)
                elif i>TinyStatistician.median(x):
                    q2list.append(i)
            return (TinyStatistician.median(q1list),TinyStatistician.median(q2list))
        except Exception:
            raise TypeError('x should be a non-empty int/float list or array.')
    @staticmethod
    def var(x):
        if not len(x):
                return None
        try:
            mean=TinyStatistician.mean(x)
            return(float((sum(map(lambda x: (x-mean)*(x-mean),x)))/len(x)))
        except Exception:
            raise TypeError('x should be a non-empty int/float list or array.')
    @staticmethod
    def std(x):
        if not len(x):
                return None
        try:
            return float(sqrt(TinyStatistician.var(x)))
        except Exception:
            raise TypeError('x should be a non-empty int/float list or array.')

test=TinyStatistician()
l=[1,42,300,10,59]
print(test.mean(l))
print(test.median(l))
print(test.quartile(l))
print(test.var(l))
print(test.std(l))
