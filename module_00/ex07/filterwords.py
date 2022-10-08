from sys import *

if len(argv)!=3:
    print("ERROR")
    exit()
if not argv[2].isdigit():
    print("ERROR")
    exit()
wordlist = [word for word in ("".join((char if char.isalpha() else" ")for char in argv[1]).split()) if len(word)>int(argv[2])]
print(wordlist)