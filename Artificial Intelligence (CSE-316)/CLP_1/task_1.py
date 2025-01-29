numbers=map(int,input('Enter the numbers:').split())

sum_of_odd =0
sum_of_even=0

for number in numbers:
    if number % 2 == 0:
        sum_of_even += number
    else:
        sum_of_odd += number

print('sum of even:',sum_of_even)
print('sum of odd:',sum_of_odd)
