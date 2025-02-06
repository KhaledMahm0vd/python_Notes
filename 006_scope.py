def spam():
    global eggs
    eggs = 'Hello'  # since it is global, first one will be printed
    print(eggs)
eggs = 42
spam()
print(eggs)
