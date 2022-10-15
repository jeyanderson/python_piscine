import numpy as np

class ScrapBooker():
    def __init__(self):
        pass
    def crop(self,array,dim,position=(0,0)):
        if not isinstance(array,np.ndarray):
            return None
        if not isinstance(dim,tuple)or not isinstance(dim[0],int)or not isinstance(dim[1],int)or dim[0]<0 or dim[1]<0:
            return None
        if not isinstance(position,tuple)or not isinstance(position[0],int)or not isinstance(position[1],int)or position[0]<0 or position[1]<0:
            return None
        (x,y)=position
        (n,m)=dim
        return array[x:x+n,y:y+m]
    def thin(self,array,n,axis):

    def juxtapose(self,array,n,axis):

    def mosaic(self,array,dim):
