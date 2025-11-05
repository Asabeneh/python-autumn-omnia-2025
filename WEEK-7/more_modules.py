import os
import random
import math

def list_directories():
    lst_dir = os.listdir()
    for item in lst_dir:
        if item.endswith('.py'):
            print(item)
            f = open(f'./{item}', encoding='utf-8')
            print(f.read())
    
print(dir(random))
print(math.floor(random.random() * 11)) # 0*11 to 0.99999*11 = 9.9999999
# I want to generate 0 to 10
print(random.randint(50, 100))

def lottery_number_generator():
    lottery_numbers = []
    for i in range(6):
        random_number = random.randint(0, 100)
        lottery_numbers.append(random_number)
    return lottery_numbers

def unique_id_generator(n = 6):
    id = ''
    for _ in range(n):
        random_value = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')
        id = id + random_value
    return id
        
print(unique_id_generator())
print(unique_id_generator(16))
print(unique_id_generator(24))
print(unique_id_generator(64))
print('30 Days of Python'.lower().replace(' ', '-'))

courses = ['30 Days of Python', '30 Days of JavaScript']
if  '30 Days of Python' not in courses:
    slug = '30 Days of Python'.lower().replace(' ', '-')
else:
    slug = '30 Days of Python'.lower().replace(' ', '-') + '-' + unique_id_generator(6)
print(slug)


    