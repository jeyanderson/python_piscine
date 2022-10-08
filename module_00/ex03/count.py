from curses.ascii import isspace
import sys


def text_analyzer(pstr=""):
    """
    fuction that take a single string argument(pstr) and displays the sums of its upper-case characters, lower-case characters, punctuation
    characters and spaces.
    """
    c_valid=".,?!-*'"
    if type(pstr)!=str:
        print("message isnt a string.")
        exit()
    if(len(pstr)==0):
        pstr = input("please provide a string.\n>> ")
    s_count=u_count=l_count=c_count=0
    for i in range(0,len(pstr)):
        if pstr[i].isspace():
            s_count+=1
        elif pstr[i].isupper():
            u_count+=1
        elif pstr[i].islower():
            l_count+=1
        elif c_valid.find(pstr[i])==1:
            print(pstr[i])
            print(c_valid.find(pstr[i]))
            c_count+=1
    print("The text contains ",len(pstr)," character(s):")
    print("- ",u_count," upper letters(s)")
    print("- ",l_count," lower letters(s)")
    print("- ",c_count," ponctuation mark(s)")
    print("- ",s_count," space(s)")

def main():
    if len(sys.argv)==2:
        text_analyzer(sys.argv[1])
    elif len(sys.argv)!=2:
        print("too many/few args.")

if __name__ == '__main__':
    main()