kata=(19,42,21)
a=[]
print("The "+str(len(kata))+" numbers are: ",end="")
for var in range(len(kata)):
    a.append(str(kata[var]))
print(", ".join(a))