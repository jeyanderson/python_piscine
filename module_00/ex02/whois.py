import sys

if len(sys.argv)<2:
    exit()
if len(sys.argv)>2:
    print('Too many arguments.')
    exit()
if not sys.argv[1].isdigit():
    print("Not an int.")
    exit()
value=int(sys.argv[1])
if value==0:
    print("I'm Zero.")
    exit()
print("I'm Even.") if value%2==0 else print("I'm Odd.")
