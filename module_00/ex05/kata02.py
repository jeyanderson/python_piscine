kata = (2019,9,25,3,30)

month=str(kata[1]) if kata[1]/10>=1 else "0"+str(kata[1])
hour=str(kata[3]) if kata[3]/10>=1 else"0"+str(kata[3])
day=str(kata[2]) if kata[2]/10>=1 else"0"+str(kata[2])
min=str(kata[4]) if kata[4]/10>=1 else"0"+str(kata[4])
print(month+"/"+day+"/"+str(kata[0])+" "+hour+":"+min)