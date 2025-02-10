print('provide a list of numbers:')
initial_list=list(map(int,input().split()))
unique_list=list(set(initial_list))
unique_list.sort()

print('Unique & Sorted List:',unique_list)
