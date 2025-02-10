numbers=list(map(int,input('Enter the numbers:').split()))

for i in range (len(numbers)):

    for j in range (len(numbers)-i-1):
        if numbers[j] < numbers[j+1]:
            temp=numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp

print('Second Highest',numbers[1])
