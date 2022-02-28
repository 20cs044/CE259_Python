# Practical AIM             :-  c. Write a Python program to sum all the items in a dictionary.
# Student-ID                :-  20CS044
# Student-Name              :-  DEVRAJ PARMAR
# GitHub repository link    :-  https://github.com/20cs044/CE259_Python.git

Dict1= {
    'a': 23,
    'b': 12,
    'c': 19,
    'd': 55,
    'e': 76
}

sum=0;                  #initialize sum
for i in Dict1:         #for loop to sum all the items in a dictionary
    sum=sum+Dict1[i]

print(sum)
