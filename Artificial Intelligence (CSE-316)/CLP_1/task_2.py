numbers=list(map(int,input('Enter the numbers:').split()))

min=numbers[0]

for i in numbers:
    if i < min:
        min=i

print('smallest number is:',min)
