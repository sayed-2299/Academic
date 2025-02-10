import numpy as np

matrix=np.random.randint(1,11 ,size=(5,5))
sum=np.sum(matrix , axis=1)

print(matrix,"\n")
print("row wise sum is:",sum)