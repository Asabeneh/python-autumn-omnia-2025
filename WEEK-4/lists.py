'''
List is an ordered, index items. It can be mutated or modified

'''

empty_lst = []
print(type(empty_lst))

num_1 = [1, 2, 3, 4, 4]
num_2 = [5, 5, 6, 7, 8, 9, 10]

print(num_1)
print(len(num_2))
print(num_1 + num_2)
names = ['Zoom User','Marian','Blake', 'Eelon','Kinta']
list_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

shopping_list = ['Milk','Bread','Bread', 'Potatoes','Coffee','Tea', 'Sugar']

print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[-1])
print(shopping_list[0:5])

shopping_list[0] ='Soya Milk'
print(shopping_list)
shopping_list[-1]  = 'Honey'

print(shopping_list)

shopping_list.append('Meat')

print(shopping_list)
shopping_list.append('Cheese')
print(shopping_list)

shopping_list.pop(-2)
print(shopping_list)
shopping_list.insert(3, 'Mango')

print(shopping_list)
shopping_list.remove('Coffee')
print(shopping_list)
print(shopping_list.count('Bread'))


print(shopping_list)
print(shopping_list.index('Mango'))
# print(shopping_list.find('Lemon'))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print(fruits + vegetables)
fruits.extend(vegetables)
print(fruits)

shopping_list_copy_1 = shopping_list.copy()
shopping_list_copy_1.reverse()
print(shopping_list_copy_1)
print(shopping_list)

shopping_list_copy_2 = shopping_list.copy()
shopping_list_copy_2.sort(reverse=True)
print(shopping_list_copy_2 )
print(shopping_list)

shopping_list.clear()
print(shopping_list)

nums = [1, 2, 3, 4, 5]

print(nums[2:4])

"""
 Break: 
 8:06
"""