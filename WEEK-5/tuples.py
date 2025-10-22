'''
- Number(int, float, complex)
- Boolean(True, False)
- String
- List - order item, indexed, mutated(modifiable)
- Tuple - ordered, index, immutable(unmodifiable)
- Set - not order, no indexing, mutable
- Dictionary - key and value, access values by key
'''

# How to create tuple

empty_tuple = ()
print(empty_tuple, type(empty_tuple))

nums = (1, 2, 3)
print(nums, type(nums))

# Tuple with only one item

one_item_tuple = (10,)
print(one_item_tuple, type(one_item_tuple))

print(one_item_tuple[0])

# Type casting: converting one data type to another 
metropolitans = ('Helsinki','Espoo','Vanta','Kurkoniemi','Kaunainen')
print(metropolitans[0])
print(metropolitans[1])
print(metropolitans[-1])
print(metropolitans[1:4])
print(metropolitans.index('Espoo'))

nums = (1, 3, 3, 2, 4, 5, 5, 9)
print(nums)
print(nums.count(5))

nums_lst = list(nums)
print(nums_lst)
nums_lst.append(-5)
print(nums_lst)
print(nums)
nums_set = set(nums)
print(nums_set)

print('Nums:', nums)
print('The length or size of nums:', len(nums))
print('The number of 3 in the nums:', nums.count(3))

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

lst = [1, 2, 3]

print(lst)
lst.pop()
print(lst)
lst.clear()
print(lst)
