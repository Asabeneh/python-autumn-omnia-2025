first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name  +  " " + last_name
print(full_name)

print('I love people.\nI love Python.\nI love everyhting.')
print('Name\tAge\tCountry\tWeight')
print('John\t20\tFinland\t62')
print('David\t25\tUK\t65')

print('Why is not possible to write this symbol(\) in old python versions.')
print('Why is not possible to write this symbol(\\) in old python versions.')
print('Some people say "an apple a day keep the doctor away"')
print("Some people say \"an apple a day keep the doctor away\"")
print('I don\'t like coffee or tea')
print("I don't like coffee or tea")

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
age = 250
height = 1.73

""" formated_string = 'I am %s %s. I teach %s. I am %d years old. I am %.2f meter tall.' %(first_name, last_name, language, age, height)
print(formated_string) """

""" formated_string = f'I am {first_name} {last_name}. I teach {language}. I am {age} years old. I am {height} meter tall.'
print(formated_string) """


# formated_string = 'I am {} {}. I teach {}. I am {} years old. I am {} meter tall.'.format(first_name, last_name, language, age, height)
# print(formated_string) 


formated_string = f'I am {first_name} {last_name}. I teach {language}. I am {age} years old. I am {height} meter tall.'
print(formated_string)


a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print(f'{a} / {b} = {a / b :.2f}')
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


# String as a sequence of characters

language = 'Python'
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
print(len(language))

last_index = len(language) - 1
print(language[last_index])

print(language[-1])
print(language[-6])
print(language[1:6])
print(language[1:])
print(language[2:5])
print(language[-4:-1])
print(language[::-1])

txt = '  I love people, love is great  '
print(txt.upper())
print(txt.lower())
print(txt.swapcase())
print(txt.title())
print(txt.split())
print(txt.replace('people','Python'))
print(txt.lstrip())
print(txt.strip())
print(txt.count('o'))
print(txt.count('e'))
print(txt.count('love'))


dna = '''
GGCTGTGCTTGGAGTCAATCGCAAGTAGGATGGTCTCCAGACACCGGGGCACCAGTTTTCACGCCGAAAGCATAAACGACGAGCAGATATGAAAGTGTTAGAACTGGACGTGCCGTTTCTCTGCGAAGAACACCTCGAGCTGTAGCGTTGTTGCGCTGCCTAGATGCAGTGTTGCTCATATCACATTTGCTTCAACGACTGCCGCCTTCGCTGTATCCCTAGACACTCAACAGTAAGCGCTTTTTGTAGGCAGGGGCACCCCCTATCAGTGACTGCGCCAAAACATCTTCGGATCCCCTTGTCCAATCAAACTCATCGAATTCTTACATTTAAGACCCTAATATCACATCATTAGTGATTAATTGCCACTGCCAAAATTCTGTCCAGAAGCGTTTTAGTTCGCTCCACTAAAGTTGTTTAAAACGACTACCAAATCCGCATGTTAGGGGATTTCTTATTAATTCTTTTATCGTGAGGAACAGCGGATCTTAATGGATGGCCGCAGGTGGTATGGAAGCTAATAGCGCGGGTGAGAGGGTAATCAGCCGTGTTCACCTACACAACGCTAACGGGCGATTCTATAAGATTCCGCATTGCGTCTACTTATAAGATGTCTCAACGGTATCCGCAACTTGTGAAGTGCCTACTATCCTTAAACGCATATCTCGCCCAGTAGCTTCCCAATATGTGAGCATCAATTGTTGTCCGGGCCGAGATAGTCATGTGCTCACGGAACTTACTGTATGAGTAGTGATTTGAAAGAGTTGTCAGTTTGCTGGTTCAGGTAAAGGTTCCTCACGCTACCTCAAAGTAAGAGAGCGGTCGTGACATTATCCGTGATTTTCTCACTACTATTAGTACTCACGACTCGATTCTGCCGCAGCCATGTTTCGCCAGAATGCCAGTCAGCATTAAGGAGAGCTCAGGGCAGGTCAACTCGCATAGTGAGGGTTACATGTTCGTTGGGCTCTTCCGACACGAACCTCAGTTAGCCTACATC
'''
total = len(dna)
total_a = dna.count('A')
print(total, total_a, total_a / total * 100)
'''

Break: 10 minutes
18: 47

'''

print('Finland'.endswith('land'))
challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs(15))

txt = 'love is great'

print(txt.rfind('e'))
print(txt.rindex('e'))
print('cat'.isalpha())
print('cat'.isalnum())
print('cat'.isnumeric())
print('123'.isnumeric())
print('123'.isdigit())

challenge = '\u00B2'
print(challenge.isdigit())   # False

num = '10.5'
print(num.isnumeric()) # False

countries = ['Finland', 'Sweden', 'Norway']
print(', '.join(countries))

print('Finland'.startswith('F'))
print('Finland'.startswith('Fin'))


statement = '''
I love people, because it is so great.
'''
print(f'''I love {language}, because it is so great.''')


'''
I love people, because it is so great.
'''

