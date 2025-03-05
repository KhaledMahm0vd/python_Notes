# dict[key] --> value
# dictionaries are unordered.
# order matters for lists but it does not for dictionaries.
myCat = {'size':'fat', 'color':'gray', 'voice':'loud'}
print(myCat['size'])
print('my cat has '+myCat['color']+' fur')
# list order:
print([1,2,3] == [3,2,1])
# dictionary order:
eggs = {'count':4, "color":"red", "age":1}
ham = {"age":1, "count":4, "color":"red"}
print(eggs == ham)
print('name' in eggs)
print('color' in ham)
print('count' not in eggs)

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k,v in eggs.items():
    print(k,v)

