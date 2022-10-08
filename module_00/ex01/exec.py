import sys


if len(sys.argv) < 2:
    exit()
words = ""
i = 1
while i<len(sys.argv)-1:
    words+=sys.argv[i]
    words+=" "
    i+=1
words+=sys.argv[i]
words = words [::-1].swapcase()
print(words)