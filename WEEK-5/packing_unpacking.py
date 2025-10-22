
# a, b, c = 10, 20, 30
a = 10
b = 20
c = 30
print('a:', a)
print('b:', b)
print('c', c)
a, _, c = (10, 20, 30)
print(a, c)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']
fin, swe,*rest = countries
print(fin)
print(swe)
print(rest)

nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]
some_lst = [-3, -2, 1, 0]
# nums = nums1 + some_lst+ nums2
nums = [*nums1, *some_lst, *nums2]
print(nums)