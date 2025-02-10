numbers=map(int,input('Enter Numbers:').split())

def task_8(numbers):
    sum=0
    for num in numbers:
        sum = sum + num
    return sum

print('Sum:',task_8(numbers))
