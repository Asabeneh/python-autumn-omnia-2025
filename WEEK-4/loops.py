
""" print(range(0, 3, 1))
print(range(3))
print(list(range(3)))
print(list(range(10, 101, 10)))
print(list(range(0, 101, 2)))
print(list(range(1, 101, 2)))
print(list(range(100, 1001, 100))) """


""" for i in range(11):
    print(f'{i} x {i} = {i * i}')
    
    
for i in range(1, 1001):
    print(f'{i} - Hello, world!') """
    

# for i in range(6):
#     print(i)

""" word = 'Finland'
txt = ''
for i in range(len(word)-1, -1, -1):
    txt = txt  + word[i]
print(txt)

for i in range(5, -1, -1):
    print(i) """
    
    
    
nums = [5, -3, 2, 0, 10, -4, 8, 7, 6, 1]

positive_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)
print(positive_nums)


even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print(even_nums)


for num in nums:
    if num < 0:
        break 
    print(num)
    
    
for num in nums:
    if num >= 0:
        continue
    print(num)
    
    
# While loop

""" user_password = '123'

while True:
    password = input('Your password: ')
    if password == user_password:
        print('Welcome back to your Dashboard')
        break """
    
count = 0 

while count < 11:
    print(count)
    count = count + 1
    
    
count = 10

while count >= 0:
    print(count)
    count = count - 1


'''
Number guess game
'''