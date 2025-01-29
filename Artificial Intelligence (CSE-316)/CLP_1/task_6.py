n=int(input('Enter the number:'))
num1=0
num2=1

print('Series:',end=' ')

print(num1,end=' ')
print(num2,end=' ')

for i in range(3,n+1):
    print(num1+num2,end=' ')

    temp=num1+num2
    num1=num2
    num2=temp
