import numpy as np
matrix=np.random.randint(0,101,(5,5))
print(matrix)
sum=0
oszlop=np.max(matrix,axis=0)
for i in oszlop:
    sum+=int(i)
    #print (i)
sor=np.max(matrix,axis=1)
for i in sor:
    sum+=int(i)
    #print(i)

print(sum)