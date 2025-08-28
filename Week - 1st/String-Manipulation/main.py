"""
String is immutable
"""
txt = 'My name is Pritam'
print(len(txt))
print('Pritam' in txt)
print('hello' not in txt)

name = 'Pritam'
age = 24
print(f'My name is {name} and my age is {age}')  # fstring
print('My name is {} and my age is {}'.format(name, age))  # formatting
