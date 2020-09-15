from decode import *
from constants import *

# unknown bits will be filled with 'x'
# expecting 48 bit key
def removeCompression(round3Key):
    dict = {}
    for i in range(56):
        dict[i] = 'x'
    for i in range(48):
        dict[pc2[i]-1] = round3Key[i]
    temp = ''
    for i in range(56):
        temp += dict[i]
    return temp

# expecting 54 bit key
def applyCompression(left, right):
    temp = ''
    key = left + right
    for i in range(48):
        temp += key[pc2[i]-1]
    #print(temp)
    return temp

def splitHalf(str):
    return str[:28], str[28:]

def cirShiftRight(str, pos):
    return str[-pos:] + str[:-pos]

def cirShiftLeft(str, pos):
    return str[pos:] + str[:pos]


def get56bitKeyReverseEngineering():
    temp1 = removeCompression(keys[2])
    # leftHalf, rightHalf = splitHalf(temp1)
    # l1 = cirShiftRight(leftHalf, 4)
    # r1 = cirShiftRight(rightHalf, 4)
    # print(leftHalf, rightHalf)
    # print(l1, r1)
    # print(l1+r1)
    return temp1

key3_56 = get56bitKeyReverseEngineering()
print(key3_56)
# def get64bitKey(key_56):
#     key = ''
#     dict = {}
#     for i in range(64):
#         dict[i] = 'x'
#     for i in range(56):
#         dict[pc1[i]-1] = key_56[i]
#     # print(dict)
#     for i in range(64):
#         key += dict[i]
#     # print(key)
#     return key
# get64bitKey(key3_56)
# print(get64bitKey(key3_56))
###############generate key###############

# expecting 56 bit key after dropping parity
# starting to create 
# def createRoundKey(temp):
#     roundKey = [[] for i in range(3)]
#     left, right = splitHalf(temp)
#     left = cirShiftLeft(left, 1)
#     right = cirShiftLeft(right, 1)
#     roundKey[0] = applyCompression(left, right)
#     left = cirShiftLeft(left, 1)
#     right = cirShiftLeft(right, 1)
#     roundKey[1] = applyCompression(left, right)
#     print(temp)
#     print(left, right)
#     left = cirShiftLeft(left, 2)
#     right = cirShiftLeft(right, 2)
#     roundKey[2] = applyCompression(left, right)
#     return roundKey

# createRoundKey(key3_56)

