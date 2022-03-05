# Practical AIM             :-  Some words may repeat,output its number of occurrences.
# Student-ID                :-  20CS044
# Student-Name              :-  DEVRAJ PARMAR
# GitHub repository link    :-  https://github.com/20cs044/CE259_Python.git


import collections

N = int(input())
d = collections.OrderedDict()

# for loop for taking n words as input.
for i in range(N):
    word = input()
    # condition for checking the occurrences of each word.
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(len(d))

for k, v in d.items():
    print(v, end=" ")
