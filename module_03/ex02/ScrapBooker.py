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
        if not isinstance(array,np.ndarray):
            return None
        if not isinstance(n,int)or n<1:
            return None
        if not isinstance(axis,int)or axis not in[0,1]:
            return None
        return array[[i for i in range(array.shape[0])if(i+1)%n]] if axis else array[:,[i for i in range(array.shape[1])if(i+1)%n]]
    def juxtapose(self,array,n,axis):
        if not isinstance(array,np.ndarray):
            return None
        if not isinstance(n,int)or n<1:
            return None
        if not isinstance(axis,int)or axis not in[0,1]:
            return None
        return np.hstack([array]*n) if axis else np.vstack([array]*n)
    def mosaic(self,array,dim):
        if not isinstance(array,np.ndarray):
            return None
        if not isinstance(dim,tuple)or not isinstance(dim[0],int)or not isinstance(dim[1],int)or dim[0]<0 or dim[1]<0:
            return None
        new_arr=self.juxtapose(array,dim[0],0)
        new_arr=self.juxtapose(new_arr,dim[1],1)
        return new_arr
        

test=ScrapBooker()
array=np.arange(0,25).reshape(5,5)
# print(test.crop(array,(3,1),(1,2)))
array=np.array('A B C D E F G H I'.split()*6).reshape(-1,9)
print(test.thin(array,3,0))
array=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(test.juxtapose(array,2,1))
array=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(array)
print(test.mosaic(array,(2,2),))