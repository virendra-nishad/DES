from constants import *
from removePermutation import *
from boxProperty import *
import numpy as np

key_matrix = np.zeros((8, 64), dtype=int)
keys = [[] for i in range(3)]



def changeIOForm():
    file1_w = open("input1.txt", 'w')
    file2_w = open("output1.txt", 'w')
    with open('input.txt') as file1_r, open('output.txt') as file2_r:
        flag = 0
        temp1 = ''
        temp2 = ''
        for in_line, out_line in zip(file1_r, file2_r):
            if flag == 0:
                temp1 = in_line.split('\n')[0]
                temp2 = out_line.split('\n')[0]
                flag = 1
            else:
                file1_w.write(temp1 + ":" + in_line)
                file2_w.write(temp2 + ":" + out_line)
                flag = 0
    file1_r.close()
    file2_r.close()
    file1_w.close()
    file2_w.close()

changeIOForm()

def removeRoundPerm(input_str):
    temp = ''
    for i in range(len(input_str)):
        temp += input_str[perm[i]-1]
    return temp

def applyExpansion(input_str):
    temp = ''
    temp += input_str[-1] + input_str[0:5] + input_str[3:9] + input_str[7:13]
    temp += input_str[11:17]+input_str[15:21]+input_str[19:25]+input_str[23:29]
    temp += input_str[27:32] + input_str[0]
    return temp


def generateKey():
    # input.txt and output.txt initial and final permutation removed
    with open('input1.txt') as file1_r, open('output1.txt') as file2_r:
        for in_line, out_line in zip(file1_r, file2_r):
            #print("{0}\t{1}".format(in_line.strip(), out_line.strip()))
            temp = in_line.split('\n')[0] #remove newline
            input_pair = temp.split(':')  # get input pair conatining same right half
            temp = out_line.split('\n')[0]  #remove newline
            output_pair = temp.split(':')   # get cipher pair of above input pair
            print(input_pair[0], input_pair[1], output_pair[0], output_pair[1])

            input_pair_bin = [[] for i in range(2)]
            input_pair_bin[0] = getInBinaryForm(input_pair[0])
            input_pair_bin[1] = getInBinaryForm(input_pair[1])
            
            output_pair_bin = [[] for i in range(2)]
            output_pair_bin[0] = getInBinaryForm(output_pair[0])
            output_pair_bin[1] = getInBinaryForm(output_pair[1])
            #print(input_pair_bin, output_pair_bin)

            output_diff = stringXor(output_pair_bin[0], output_pair_bin[1])
            input_diff = stringXor(input_pair_bin[0], input_pair_bin[1])

            #print(input_diff, output_diff)
            # below is actually f_box differential output
            # see formula for f_box_out_bin
            f_box_out_bin = stringXor(input_diff[0:32], output_diff[32:64])
            f_box_out_bin = removeRoundPerm(f_box_out_bin)
            # input for last round box is same as left half of output
            expanded_input_1 = applyExpansion(output_pair_bin[0][0:32])
            expanded_input_2 = applyExpansion(output_pair_bin[1][0:32])
            expanded_input_diff = stringXor(expanded_input_1, expanded_input_2)
            
            for i in range(8):
                # local to each box
                box_input_1 = expanded_input_1[i*6:i*6+6]
                box_input_2 = expanded_input_2[i*6:i*6+6]
                box_input_diff = expanded_input_diff[i*6:i*6+6]
                box_out = f_box_out_bin[i*4:i*4+4]
                #don't forget to take care of box number
                index1 = int(box_input_diff, 2)
                index2 = int(box_out, 2)
                # in below 'i' will select box
                possible_key = possible_key_collection[i][index1*16 + index2]
                # print(possible_key)
                for key in possible_key:
                    key1 = stringXor(key, box_input_1)
                    key2 = stringXor(key, box_input_2)
                    key1_dec = int(key1, 2)
                    key2_dec = int(key2, 2)
                    key_matrix[i][key1_dec] += 1
                    key_matrix[i][key2_dec] += 1
        print(key_matrix)

generateKey()

def gettingKey():
    index = [[] for i in range(8)]
    for i in range(8):
        mx = 0
        for j in range(64):
            if key_matrix[i][j] > mx:
                mx = key_matrix[i][j]
                index[i] = j
        count = 0
        for j in range(64):
            if key_matrix[i][j] == mx:
                count += 1
        print(index, count, mx)
    print(index)
    temp = ''
    for i in range(8):
        temp += '{0:06b}'.format(index[i])
    keys[2] = temp

gettingKey()



# def inputDifferential():
#     file_r = open('input.txt', 'r')
#     file_w = open('input_diff.txt', 'w')
#     flag = 0
#     string1 = ''
#     string2 = ''
#     for line in file_r:
#         if flag == 0:
#             string1 = line
#             flag = 1
#         else:
#             flag = 0
#             string2 = line
#             print(string1)
#             print(string2)
#             temp1 = getInBinaryForm(string1)
#             temp2 = getInBinaryForm(string2)
#             input_differential = stringXor(temp1, temp2)
#             file_w.write(input_differential + '\n')
#     file_r.close()
#     file_w.close()

# def outputDifferential():
#     file_r = open('output.txt', 'r')
#     file_w = open('output_diff.txt', 'w')
#     flag = 0
#     string1 = ''
#     string2 = ''
#     for line in file_r:
#         if flag == 0:
#             string1 = line
#             flag = 1
#         else:
#             flag = 0
#             string2 = line
#             print(string1)
#             print(string2)
#             temp1 = getInBinaryForm(string1)
#             temp2 = getInBinaryForm(string2)
#             input_differential = stringXor(temp1, temp2)
#             file_w.write(input_differential + '\n')
#     file_r.close()
#     file_w.close()

# inputDifferential()
# outputDifferential()

