#!/usr/bin/env python3
from ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load("non_existing_file.png")
# Output
# Exception: FileNotFoundError -- strerror: No such file or directory
print(arr)
# Output
# None
# arr = imp.load("empty_file.png")
# Output
# Exception: OSError -- strerror: None
print(arr)
# Output
# None
arr = imp.load("../resources/dgrfly_pfp.jpeg")
# Output
# Loading image of dimensions 270 x 270
print(repr(arr))
imp.display(arr)