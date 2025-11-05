def make_square(n):
    return n ** 2

def calcaulate_bmi(mass, height):
    """
    This function takes two parameters:mass and height.
    It returns the BMI
    """
    bmi = mass / height ** 2
    return round(bmi, 2)
    
    
def reverse_list(lst):
    '''
    The reverse_list functin take a list paramater and return the reverse list
    '''
    new_lst = []
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

def generate_countries_code(lst):
    return list(map(lambda country:country.upper()[:3], lst))

def find_world_population(data):
    from functools import reduce
    total = reduce(lambda acc, cur: acc + cur['population'], data,  0)
    return f'{total:,}'
   