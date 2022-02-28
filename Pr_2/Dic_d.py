# Practical AIM             :-  d. Write a Python script to add a key to a dictionary.
# Student-ID                :-  20CS044
# Student-Name              :-  DEVRAJ PARMAR
# GitHub repository link    :-  https://github.com/20cs044/CE259_Python.git

#example_1
print("\nexample 1 : ")
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dict = {
    0: 10,
    1: 20
}
print("before updating")
print(dict)
dict.update({2: 30})    #adding one key in dict using .update()
print("after updating")
print(dict)

#example_2
print("\nexample 2 : ")
# Another example for above question

student_ = {
    'Id': 'ab123',
    'Name': 'abc',
    'Age': '19'
}

print("before updating")
print(student_)
student_.update({'roll_no':52})
print("after updating")
print(student_)
