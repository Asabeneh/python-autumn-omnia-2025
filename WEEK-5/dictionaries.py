"""
Dicitoanry is a python data time structure in key and value format
"""
empty_dct = {}
print(empty_dct, type(empty_dct))

user = {
  'first_name':'Asab',
  'email':'asab@gmail.com',
  'password':'123123',
  'logged_in':False,
  'created_at':'22/10/2025 18:59',
  'skills':['HTML','CSS','JS']
}

person = {
  'first_name':'Asabeneh',
  'last_name':'Yetayeh',
  'age':250,
  'country':'Finland',
  'is_married':True,
  'height':1.72,
  'skills': ['HTML','CSS','JS', 'Python'],
  'qualifications':('BSc','MSc')
  }

print(person)
print(person['first_name'])
print(person['last_name'])
print(person.get('email'))
person['age'] = 60
person['hobbies'] = ['Hiking', 'Running']

print(person)
person['skills'].append('MySQL')

print(person)

print(len(person))
print('first_name' in person)
person['email'] = 'asab@gmail.com'
print('email' in person)

if 'hobbies' in person:
  print(person['hobbies'])
else:
  print('The person does not have any hobbies')
  
# person.pop('age')
""" if 'age' in person:
  del person['age']
  print(person) """
  
for key in person:
  print(key, person[key])
  
items = person.items()
print(items)

""" for item in items:
  key = item[0]
  value = item[1]
  print(item, key, value) """
  
for key, value in items:

  print( key, value)
  
# items, keys, values
keys = person.keys()
print(keys)

values = person.values()
print(values)

person_copy = person.copy()

person_copy['title']  = 'Fullstack Developer'

print(person_copy)
print(person)