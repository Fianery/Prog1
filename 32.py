out_file=open("piramis.txt","w")
n=int(input("szam: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):                #ures helyek
        print(end=" ",file=out_file)
    for j in range(i,0,-1):                 #ertekek
        print(j,end="",file=out_file)
    for j in range(2,i+1):                  #jobb
        print(j,end="",file=out_file)
    print("\n",file=out_file)
out_file.close()
