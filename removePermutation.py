# This part of program will import data from 
# 1. genText.py
#   input_set, bit_set

from genText import *
from constants import *

def get_key(val): 
    for key, value in alphabet_map.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"


def getInBinaryForm(string_data):
    in_binary = ""
    for i in range(len(string_data)):
        if string_data[i] != '\n':
            in_binary += alphabet_map[string_data[i]]
    return in_binary

def getInAlphabetForm(binary_data):
    in_alphabet = ""
    count = 0
    while count < len(binary_data):
        in_alphabet += get_key(binary_data[count : count+4])
        count += 4
    return in_alphabet

def removeInitialPermutation(binary_string_input):
    temp_string = ""
    for i in range(len(binary_string_input)):
        temp_string += binary_string_input[ip[i]-1]
    return temp_string

def removeInverseInitialPermutation(binary_string_input):
    temp_string = ""
    for i in range(len(binary_string_input)):
        temp_string += binary_string_input[ipinv[i]-1]
    return temp_string
