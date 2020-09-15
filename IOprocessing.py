from removePermutation import *
import os

# apply anti permutation 

def applyAntiInitialPerm():
    file_r = open('rand_text.txt')
    file_w = open("input.txt", 'w')
    for line in file_r:
        temp = getInBinaryForm(line)
        temp = removeInitialPermutation(temp)
        temp = getInAlphabetForm(temp)
        file_w.write(temp + "\n")
    file_r.close()
    file_w.close()

applyAntiInitialPerm()

def applyAntiFinalPerm():
    file_r = open('response.txt')
    file_w = open('output.txt', 'w')
    for line in file_r:
        temp = getInBinaryForm(line)
        temp = removeInverseInitialPermutation(temp)
        temp = getInAlphabetForm(temp)
        file_w.write(temp + "\n")
    file_r.close()
    file_w.close()


# def getUniqueChar():
#     string = 'aabbcd'
#     unique = []
#     file_r = open('input.txt')
#     for string in file_r:
#         string = string.split('\n')[0]
#         for char in string[::]:
#             if char not in unique:
#                 unique.append(char)
#     print(unique)
# getUniqueChar()
# # applyAntiFinalPerm()
