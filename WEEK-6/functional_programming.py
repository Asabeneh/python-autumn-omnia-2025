"""
map, filter, reduce

"""

""" def double_list(lst):
    new_lst = []
    for num in lst:
        doubled = num * 2
        new_lst.append(doubled)
    return new_lst
nums = [1, 2, 3, 4] # [2, 4, 6, 8]
print(double_list(nums))
print(double_list([5, 10, 15, 20])) """

def reverse_list(lst):
    new_lst = []
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

nums = [1, 2, 3, 4]
countries = ['Finland','Sweden','Norway','Denmark','Iceland']
# print(reverse_list(nums))
# print(reverse_list(countries))

doubled_numbers = list(map(lambda n: n + 100, nums))
# print(doubled_numbers)

def generate_countries_code(lst):
    return list(map(lambda country:[country, country.upper(), country.upper()[:3], len(country)], lst))

from countries import countries
from countries_data import countries_data
from pprint import pprint

# pprint(generate_countries_code(countries))


# def filter_evens(lst):
#     evens = []
#     for num in lst:
#         if num % 2 == 0:
#             evens.append(num)
#     return evens

# nums = [0, 3, -2, 4, 5, 2, 6, 7]
# print(filter_evens(nums))

nums = [0, 3, -2, 4, 5, 2, 6, 7]
evens = list(filter(lambda n: n % 2 != 0, nums))
# print(evens)

for country in countries:
    if 'land' in country:
        pass
        # print(country)

# countries_with_land = list(filter(lambda country: 'land' in country, countries))
# print(countries_with_land)

# pprint(countries_data)
# for country in countries_data:
#     if country['population'] < 1000:
#         pprint(country)
        
# countries_less_1000_pop = list(filter(lambda country: country['population'] < 1000, countries_data))
# pprint(countries_less_1000_pop)

from functools import reduce

nums = [1, 2, 3, 4]

# total  = 0 
# for num in nums:
#     total +=  num 
    
# print(total)

total = reduce(lambda acc, cur: acc + cur, nums, 0)
print(total)

populations = list(map(lambda country: country['population'], countries_data))
world_population = sum(populations)
print(f"{world_population:,}")

world_population = reduce(lambda acc, cur: acc + cur['population'], countries_data,  0)
print(f"{world_population:,}")