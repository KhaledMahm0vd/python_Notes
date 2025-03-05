# change in first list does not change a copy
# but changing a copy does change the original
# since the copy and the original refers to same place in memory.
print('does not change the copy\n')
#spam refers to a reference of the list not the actual list.
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)
print('does change the copy\n')
listx = [0,1,2,3,4]
choice = listx
choice[1] = 'hello!'
print(choice)
print(listx)
