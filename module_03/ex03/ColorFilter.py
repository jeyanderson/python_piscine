from tkinter import Image
import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter():
    def invert(self,array):
        if not isinstance(array,np.ndarray):
            return None
        return 1-array
    def to_blue(self,array):
        if not isinstance(array,np.ndarray):
            return None
        (x,y,_)=array.shape
        zero=np.zeros((x,y,2))
        zero=np.dstack((zero,array[:,:,2]))
        return zero
    def to_green(self,array):
        if not isinstance(array,np.ndarray):
            return None
        cpy=array.copy()
        cpy[:,:,:]=0
        cpy[:,:,1]=1
        return cpy*array
    def to_red(self,array):
        if not isinstance(array,np.ndarray):
            return None
        return array-self.to_blue(array)-self.to_green(array)
    def to_celluloid(self,array):
        if not isinstance(array,np.ndarray):
            return None
        n_shades=4
        shades=np.linspace(0,1,n_shades+1)
        for i in range(n_shades):
            shade_index=(array>=shades[i])&(array<=shades[i + 1])
            array[shade_index]=shades[i]
        return array
    def to_grayscale(self,array,filter,**kwargs):
        if not isinstance(array,np.ndarray):
            return None
        if filter not in['m','mean','w','weight','weighted']:
            return None
        if filter in ['m','mean']:
            m=array.sum(axis=2)/3
            return np.dstack((m,m,m))
        else:
            if 'weights' not in kwargs or not isinstance(kwargs['weights'],list) or len(kwargs['weights'])!=3:
                return None
            weights=kwargs['weights']
            return self.to_grayscale(weights*array,'m')

test=ColorFilter()
imp=ImageProcessor()
array=imp.load('../resources/desert.jpeg')
imp.display(test.to_grayscale(array,'w',weights=[0.0,0.7,0.3]))