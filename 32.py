out_file=open("piramis.txt","w")
n=int(input("szam: "))
for i in range(0,n+1):
    for j in range(0,n-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="",file=out_file)
    for j in range(2,i+1):
        print(j,end="",file=out_file)
    print("\n",file=out_file)
out_file.close()