'''
List comprehension is optimised, memory efficient way to solve problem

'''
from countries import countries
from countries_data import countries_data
from pprint import pprint

nums = [1, 2, 3, 4] # [2, 4, 6, 8]

new_lst = []

for num in nums:
    new_lst.append(num * 2)
print(new_lst)

doubled_nums = list(map(lambda num: num * 2, nums))
print(doubled_nums)

print([num + 100 for num in nums])

print([country.upper()[:3] for country in countries if 'land' in country])

nums =[[1, 2, 3], [4, 5, 6], [7, 8, 9]] # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([num for items in nums for num in  items])

""" flattened_lst = []
for lst in nums:
    for num in lst:
        flattened_lst.append(num)
print(flattened_lst) """

""" flattened_lst = []
for lst in nums:
    flattened_lst.extend(lst)
print(flattened_lst) """

""" flattened_lst = []
for lst in nums:
    flattened_lst = flattened_lst + lst
print(flattened_lst) """

countries_with_land = [country for country in countries if 'land' in country]
print(countries_with_land)
pprint([{"name": data['name'],
        "capital": data['capital'],
        "population":data['population']
        } for data in countries_data if data['population'] >= 200000000])