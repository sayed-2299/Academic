num1,num2 =map(int,input("Enter two number by Space Seperated:").split())

def task_7(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

print('Largest Number:',task_7(num1,num2))
