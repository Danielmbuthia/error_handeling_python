# types of errors

# fileNotFoundError
# with open('data.txt', 'r') as file:
#     file.read()

# keyError
# a_dict = {'key': 'value'}
# var = a_dict['no_key']

# # IndexError
# list_fruits = ['banana', 'orange', 'melon']
# var = list_fruits[3]

# # TypeError
# var = 4+ '4'

# keyword used to handle exception

# try:   block of code that might cause exception
# except: block of code to run in case of exception
# else:   block of code to run if no exception
# finally: block of code to run no matter what happened

try:
    file = open('data.txt')
    a_dict = {'key': 'value'}
    var = a_dict['key']
except FileNotFoundError:
    file = open('data.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f'key {error_message} not found')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('file closed')

# raising exception

height = float(input('height'))
if height > 3:
    raise ValueError("Human height should not be more than 3 meters")
weight = int(input('weight'))
Bmi = weight / height ** 2
print(Bmi)
