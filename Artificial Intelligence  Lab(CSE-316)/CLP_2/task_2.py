list_a=["apple", "banana", "cherry",5,7,10]
list_b=["google", "microsoft", "apple",5,12,10]

print('Input is:',list_a,'\nInput is:',list_b)

set_a=set(list_a)
set_b=set(list_b)

set_c=set_a.intersection(set_b)
print('common element is:',set_c)