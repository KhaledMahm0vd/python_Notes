# deepcopy does not change the original list
import copy
spam = ['a', 'b', 'c', 'd']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
