import itertools
import sys
import os
import string
import random
input_set = ['f',   'g',   'h',   'i',   'j',   'k',   'l',  'm',    'n',   'o',  'p',   'q',   'r',   's',   't',   'u']
bit_set = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
alphabet_map = {}
binary_map = {}

def create_alphabet_map(start):
	global alphabet_map
	k=start
	for i in input_set:
		alphabet_map[i]=bit_set[k]
		k = (k+1)%16

create_alphabet_map(0)
#print(alphabet_map)
def createBinaryToAlpha():
	global binary_map
	for i in range(len(bit_set)):
		binary_map[bit_set[i]] = input_set[i]

createBinaryToAlpha()
#print(binary_map)

def gen_random_str(character_set, size):
	random_str = ''
	for i in range(size):
		character = random.choice(character_set)
		random_str += character
	return random_str

def input_pairs():
	if os.path.isfile('rand_text.txt'):
		os.remove('rand_text.txt')
	file = open('rand_text.txt','w+')
	count = 0
	while (count < 500):
		firstEightBit = gen_random_str(input_set, 8)
		secondEightBit = gen_random_str(input_set, 8)
		file.write(firstEightBit + secondEightBit + "\n")
		firstEightBit2 = gen_random_str(input_set, 8)
		file.write(firstEightBit2 + secondEightBit + "\n")
		count += 1
	file.close()

input_pairs()