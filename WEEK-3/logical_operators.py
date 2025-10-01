'''

and, or and not

I love people.
I love Python.

I use Python to build an application.
I use JavaScript to build an application

I love Python and people.
I use Python or JavaScript to build an application.

'''

print(4 > 3 and 2 > 1) # True
print(4 > 3 and 2 < 1) # False 
print(4 < 3 and 2 < 1)  # False

print(4 > 3 or  2 > 1)  # True
print(4 > 3 or 2 < 1)  # True
print(4 < 3 or 2 < 3)  # False
print(True and True)  # True
print(True and False)
print(True or False)
print(not 4 > 3)
print(not 4 < 3)
print(not not 4 > 3)
print(not True)
print(not False)
print( not 2 * 5 == 2 ** 5)
print ( not True == False)

print ( not not not not not True == False)