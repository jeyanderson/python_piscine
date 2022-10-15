from tkinter import Image
from PIL import Image
import numpy as np

class ImageProcessor():
    def __init(self):
        pass
    @staticmethod
    def load(path):
        try:
            with Image.open(path) as img:
                arr=np.array(img)/255
                print(f'Loading image of dimensions {arr.shape[0]} x {arr.shape[1]}')
                return arr
        except Exception as e:
            print(e)
    @staticmethod
    def display(array):
        array=array*255
        array=array.astype('uint8')
        im=Image.fromarray(array)
        im.show()