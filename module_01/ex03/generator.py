from random import randint

def generator(string,sep=" ",option=None):
    if not isinstance(string,str) or option not in ['shuffle','ordered','unique',None]:
        yield("ERROR")
    else:
        lst=string.split(sep)
        if option=="shuffle":
            newlst=[]
            n=len(lst)
            while n:
                newlst.append(lst.pop(randint(0,n-1)))
                n-=1
            lst=newlst
        elif option=="ordered":
            lst=sorted(lst)
        elif option=="unique":
            lst=set(lst)
        for word in lst:
            yield word

text="Le Lorem Ipsum est simlement du faux texte."
for word in generator(text,sep=" ",option="ordered"):
    print(word)

text=1.0
for word in generator(text,sep="."):
    print(word)