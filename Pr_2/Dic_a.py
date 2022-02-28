# Practical AIM             :-  a. Write a Python script to check whether a given key already exists in a dictionary.
# Student-ID                :-  20CS044
# Student-Name              :-  DEVRAJ PARMAR
# GitHub repository link    :-  https://github.com/20cs044/CE259_Python.git

# create one dictionary
student = {
    'Id': '20cs044',
    'Name': 'Devraj',
    'Age': '19',
    'gender': 'male',
    'skills': ['php', 'HTML', 'c', 'c++', 'Python']
}

print('Name' in student)        #return True because 'Name'(key) is present in dictionary
print('Address' in student)     #return False because 'Address'(key) is present in dictionary
