import sys

if len(sys.argv)!=3:
    if(len(sys.argv) == 1):
        print("Usage: python operations.py <number1> <number2>")
    else:
        print("too few/many args.")
    exit()
i=1
numbers=[]
try:
    while i<len(sys.argv):
        numbers.append(int(sys.argv[i]))
        i+=1
except ValueError:
    print("not integer value received.")
    exit()
v_quotient = numbers[0]/numbers[1] if numbers[1] != 0 else "ERROR (division by zero)"
v_modulo = numbers[0]%numbers[1] if numbers[1] != 0 else "ERROR (modulo by zero)"
print("Sum:           ", numbers[0]+numbers[1])
print("Difference:    ", numbers[0]-numbers[1])
print("Product:       ", numbers[0]*numbers[1])
print("Quotient:      ", v_quotient)
print("Remainder:     ", v_modulo)