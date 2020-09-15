from constants import *
import numpy as np
import sys

# I used below line to print full matrix as without it 
# it was printing matrix which can be adjusted to screen

np.set_printoptions(threshold=sys.maxsize)

XOR_distribution_table = [[] for i in range(8)]
possible_key_collection = [[] for i in range(8)]

# print(type(XOR_distribution_table))
# print(type(possible_key_collection))


def stringXor(str1, str2):
    temp_string = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            temp_string += '0'
        else:
            temp_string += '1'
    return temp_string

# expecting box and 6 bit input 
# will return substitution output in 4 bit binary
def boxOutput(box, input):
    row_str = input[0] + input[-1]
    col_str = input[1:5]
    row_dec = int(row_str, 2)
    col_dec = int(col_str, 2)
    out_dec = box[row_dec][col_dec]
    return '{0:04b}'.format(out_dec)

def boxDifferentialProp(box, box_number):
    diffMatrix = np.zeros((64, 16))
    sets = [set() for _ in xrange(64*16)] #creating set for storing possible key
    for i in range(64):
        for j in range(64):
            i_bin = '{0:06b}'.format(i)
            j_bin = '{0:06b}'.format(j)
            I_bin = boxOutput(box, i_bin)
            J_bin = boxOutput(box, j_bin)
            input_xor_bin = stringXor(i_bin, j_bin)
            output_xor_bin = stringXor(I_bin, J_bin)
            input_xor_dec = int(input_xor_bin, 2)
            output_xor_dec = int(output_xor_bin, 2)
            diffMatrix[input_xor_dec][output_xor_dec] += 1
            sets[input_xor_dec*16 + output_xor_dec].add(i_bin)
            # u can add any form in place of i_bin
            # for decimal use i in place of i_bin
            # inorder to access X -> Y
            # sets[X*16 + Y]
            # and the value return will be in binary not hex
            # possible keys
    XOR_distribution_table[box_number] = diffMatrix
    possible_key_collection[box_number] = sets
    # # print(diffMatrix)
    # for i in range(64):
    #     for j in range(16):
    #         print(i, j)
    #         print(sets[i*16+j])
    #     print()


def generatingBoxInformation():
    box_number = 0
    for box in sBoxes:
        boxDifferentialProp(box, box_number)
        box_number += 1


generatingBoxInformation()
# print(XOR_distribution_table[0]) #try to change index
# print(possible_key_collection)