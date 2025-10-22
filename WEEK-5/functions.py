'''

Functions:

Meet: 19:48

Functions can be builtin or custom functions

Function in python should use the key word
def
it should have a name
()
:


'''

def do_something(activity):
    print(f'I am {activity}.')


do_something('teaching')
do_something('learning')
do_something('running')
do_something('playing football')


def add_two_nums(x, y):
    total = x + y 
    print(f'The sum of {x} and {y} is {total}.')
    
add_two_nums(1, 2)
add_two_nums(-9, 99)

'''
the name is calcuate_weight
parameters: mass and gravity

calucate the person's weight on planet earth:
gravity: 9.81
mass: 75
Formula of weight = mass * gravity 


calcualte_bmi
parameters: mass and height
it should return or print the bmi
bmi formula = mass / h ** 2 

'''

def calcuate_weight(mass, gravity = 9.81, planet ='Earth'):
    weight = round(mass * gravity)
    return f'The mass of the body with {mass} Kg is {weight} N weight on {planet}.'

    
    
print(calcuate_weight(75))
print(calcuate_weight(75, 1.62,'Moon'))
print(calcuate_weight(75, 3.73,'Mars'))

print(calcuate_weight(80))
print(calcuate_weight(80, 1.62,'Moon'))
print(calcuate_weight(80, 3.73,'Mars'))


def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 20, 30, 50, 99, 200, 600, -900))


'''
calculate_area_circle
parameter: radius
return area of the area of a circle
area = pi * radius * radius
'''
def calculate_weight(mass, gravity):
    weight = mass * gravity
    return weight

mass = 75
gravity = 9.81

print(calcuate_weight(mass, gravity))
   