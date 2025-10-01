'''
Conditionals
'''

a = 'skkksksksk'
if type(a) == int:
    if a > 0:
        print(f'{a} is a positive number.')
    elif a == 0:
        print(f'{a} is a zero')
    elif a <  0:
        print(f'{a} is a negative number.')
    else:
        print(f'{a} is not number')
else:
    print(f'{a} definitely Not a number')
    
    
    

""" weather = input('What is the weather like? ').lower()

if weather == 'rainy': 
    print('Go with an umbrella or raincoat')
elif weather == 'sunny':
    print('Go out freely it is just shiny day')
elif weather == 'cloudy':
    print('It may rain and it is good to consider an umbrella')
elif weather == 'snowy':
    print('It may be slippery')
elif weather == 'foggy':
    print('There might be visibility problem.')
else:
    print('No one knows about the weather') """
    

 

if 10 % 2 == 1:
    print('10 is an even number')
    print('10 is also divisible by 2')
    print('2 is a factor of 10')
    
 
username = input('Enter username: ')   
password = input('Enter your password: ')


""" if username == 'Asab' and password == '12345':
    print(f'Welcome {username}. You are logged in')
else:
    print('Try gain! Incorrect credentials') """
    
if username == 'Asab':
    if password == '12345':
        print(f'Welcome {username}. You are logged in')
    else:
         print('Try gain! Incorrect password')      
else:
    if password != '12345':
        print('Incorrect username and password')
    else: 
        print('Try gain! Incorrect username')  