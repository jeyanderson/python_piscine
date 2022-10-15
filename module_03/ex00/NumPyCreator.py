from ast import Num
import numpy as np

class NumPyCreator():
    @staticmethod
    def is_type_consistent(iterable,tp):
        types=list(set(map(type,iterable)))
        if len(types)==1:
            return types[0]
        else:
            return None if tp in types else types[0]
    @staticmethod
    def is_valid(arg,tp):
        queue=[]
        queue.extend(arg)
        while queue:
            cons=NumPyCreator.is_type_consistent(queue,tp)
            if cons is None:
                return False
            n=len(queue)
            if cons is tp:
                if len(set(map(len,queue)))>1:
                    return False
                for _ in range(n):
                    elem=queue.pop(0)
                    queue.extend(elem)
            else:
                break
        return True
    def from_list(self,lst):
        if not isinstance(lst,list):
            return None
        if not self.is_valid(lst,list):
            return None
        return np.array(lst)
    def from_tuple(self,tpl):
        if not isinstance(tpl,tuple):
            return None
        if not self.is_valid(tpl,tuple):
            return None
        return np.array(tpl)
    def from_iterable(self,itr):
        if itr:
            return np.fromiter(itr,type(itr))
        return None
    def from_shape(self,shape,value=0):
        if not isinstance(shape,tuple)or not len(shape)==2 or not isinstance(shape[0],int)or not isinstance(shape[1],int)or shape[0]<0 or shape[1]<0:
            return None
        return np.full(shape,value)
    def random(self,shape):
        if not isinstance(shape,tuple)or not len(shape)==2 or not isinstance(shape[0],int)or not isinstance(shape[1],int)or shape[0]<0 or shape[1]<0:
            return None
        return np.random.random(shape)
    def identity(self,n):
        if n<0:
            return None
        return np.identity(n)
