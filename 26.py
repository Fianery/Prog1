lista1=[]
lista2=[]
for i in range(101010,138902): #gyök
    lista1.append(i)
for j in (lista1):
    n=j**2
    n=str(n)
    if n[0]=="1" and n[2]=="2" and n[4]=="3" and n[6]=="4" and n[8]=="5" and n[10]=="6":
        lista2.append(j)
print(lista2)
