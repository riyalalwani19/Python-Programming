Exercise 4:
The below code contains a logical error and prints 'None'. Make changes in the code to print 'from 3'

def function1(value): return value def function2(func): func() def function3(): return 'from 3'

print(function1(function2(function3)))
