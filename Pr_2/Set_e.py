# Practical AIM             :-  e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# Student-ID                :-  20CS044
# Student-Name              :-  DEVRAJ PARMAR
# GitHub repository link    :-  https://github.com/20cs044/CE259_Python.git

from collections import Counter

list_1 = [14, 24, 45, 45, 94, 19]
cntr = Counter(list_1)
#most_common(1) returns top 1 most common element with its frequency.
most_common_element,frequency = cntr.most_common(1)[0] # Return the most common element and its frequency with most_common
print("The most common element is {}, and the frequency of that element is {}".format(most_common_element, frequency))
