def divideby(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error, you can not divide by zero')
print(divideby(2))
print(divideby(12))
print(divideby(0))
print(divideby(1))
