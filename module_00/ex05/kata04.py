kata=(0,4,132.42222,10000,12345.67)

mod=str(kata[0]) if kata[0]/10>1 else"0"+str(kata[0])
ex=str(kata[1]) if kata[1]/10>1 else"0"+str(kata[1])
print("module_"+mod+", "+"ex_"+ex+" : "+str(round(kata[2],2))+", "+str("{:.2e}".format(kata[3]))+", "+str("{:.2e}".format(kata[4])))