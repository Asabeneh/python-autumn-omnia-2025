'''
Builtin functions:
print(), len(), type(), input(), int(), float(), str(), list(), min(), max(), sum(), abs(), round()

'''
# print()
print('Hello')
print()
print('Hello','World', 2025,  sep='\n')

# len() - to get the length of a sequence

print(len('cat'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3)))
print(len({1, 2, 3, 3}))
print(len({'kirja':'book', 'talo':'house','auto':'car'}))

# type - tells us the data type of a value

print(type(10))
print(type(9.81))
print(type(1 + 2j))
print(type(True))
print(type(1 > 0))
print(type('cat'))
print(type(''))

""" name = input('Enter your name: ')
birth_year = input('Enter your birth year? ')
mass = input('Enter your mass: ')
height = input('How tall are you? ')
current_year = 2025
age = current_year - int(birth_year)
print(age)

print(name)
print(type(name))
print(type(birth_year))


bmi = float(mass) / float(height) ** 2

print(f'You are {name}. You were born {birth_year} and you are {age} years old now. You are {mass} and {height}, and your bmi is {round(bmi, 2)}.') """


print(str(1) + '1')
age = 100
print(f'I am {age} years old.' )

print(list())
print(list('abcdefghijklmnopqrstuvwxyz'))
print(list('abcdefghijklmnopqrstuvwxyz'.upper()))

print(min(10, -5, 0, 20, 10, -2))
print(max(10, -5, 0, 20, 10, -2))
print(sum([10, -5, 0, 20, 10, -2]))


print(abs(-5))
print(round(9.81, 1))
print(round(3.14))