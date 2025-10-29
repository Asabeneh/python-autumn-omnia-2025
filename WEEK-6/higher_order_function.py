# y = 2x
# f(x) = 2x
# g(x)  = x2
# f(g(x)) => 2(x2)
# g(f(x)) = (2x)2 => 4x2
"""
Higher order functions are functions that take another function as a parameter or return another function

"""
def make_square(n):
    return n * n 

def make_cube(func, n):
    return func(n) * n 

print(make_square(3) * 3)
print(make_cube(make_square, 3))


def do_something():
    def shall_i_do_something():
        return 'I should do something'
    return shall_i_do_something

print(do_something()())

def do_math(n):
    def add_ten():
        return n + 10
    return add_ten

print(do_math(90)())


""" def calcuator(a, b, operation = 'add'):
    def add():
        return a + b 
    def subtract():
        return a - b 
    def multiply():
        return a * b 
    def divide():
        return a / b
    if operation == 'add':
        return add
    elif operation == 'subtract':
        return subtract
    elif operation == 'multiply':
        return multiply
    elif operation == 'divide':
        return divide
    else:
        pass

print(calcuator(4, 3)())
print(calcuator(4, 3, 'divide')()) """

def calcuator(a, b):
    def add():
        return a + b 
    def subtract():
        return a - b 
    def multiply():
        return a * b 
    def divide():
        return a / b
    
    return add() + multiply(), {
        'add':add,
        'subtract':subtract,
        'multiply':multiply,
        'divide':divide
    }

print(calcuator(4, 3)[0])




        
            