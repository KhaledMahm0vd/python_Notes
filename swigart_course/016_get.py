# default Get method for finding a key in dict without raising an error and providing default value if not found.
eggs = {'count':4, "color":"red", "age":17}
print(eggs.get('age',0))
# return an empty string if not found.
print(eggs.get('health', ""))
picnicItems = {'apples':5, 'cups':2}
print("I am bringing "+str(picnicItems.get('napkins', 0))+" napkins to the party")
if "health" not in eggs:
    eggs['health'] = 'good'

print(eggs)
# the alterantive for above if statement is setdefault method
ham = {'count':4, "age":17}
ham.setdefault('color','black')
print(ham)
