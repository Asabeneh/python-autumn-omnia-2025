'''
+: addition
-: subtraction
*: multiplication
/: division
**: exponentiation
%:  moduluous 
//: floor division
'''

a = 3
b = 4

total = a  + b
difference = a - b 
product = a * b
div = a / b 
remainder = b % a
exponentiation = a ** b # 3 * 3 * 3 * 3
floor_division = b // a 

print(f'The sum of {a} and {b} is {total}.')
print(f'The difference of {a} and {b} is {difference}.')
print(f'The product of {a} and {b} is {product}.')
print(f'The division of {a} and {b} is {div}.')
print(f'The remainder of {b} divided by {a} is {remainder}.')
print(f'{a} the power of {b} is {exponentiation}.')
print(f'The floor division of {b} and {a} is {floor_division}.')

'''
We use the curly bracket to make set,dictionary and also in strings to inject data

3 + 4  = 7
'''
print(f'{a} + {b} = {total}')
print(f'{a} - {b} = {difference}')
print(f'{a} * {b} = {product}')
print(f'{a} / {b} = {div}')
print(f'{b} % {a} = {remainder}')
print(f'{a} ^ {b} = {a ** b}')
print(f'{b} // {a} = {floor_division}')

