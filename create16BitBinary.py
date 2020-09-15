from keyGenerator import*
from genText import*

def genBin8():
    file_w = open('binary8.txt', 'w')
    for i in range(256):
        binary = '{0:08b}'.format(i)
        print(binary)
        file_w.write(binary + '\n')
    file_w.close()

genBin8()
temp_key = get56bitKeyReverseEngineering()
print(temp_key)


def generatePossible256key(temp_key):
    file_r = open('binary8.txt')
    file_w = open('binary256.txt', 'w')
    for line in file_r:
        temp = ''
        replacement_bit = 0
        for i in range(56):
            if temp_key[i] == 'x':
                temp += line[replacement_bit]
                replacement_bit += 1
            else:
                temp += temp_key[i]
        file_w.write(temp + '\n')
    file_r.close()
    file_w.close()

# temp_key is 56 bit key 48bit known and eight bit unknown
# unknown bit marked with 'x'
generatePossible256key(temp_key)

# def generatePossibalAlphakey():
#     file_r = open('binary64.txt')
#     file_w = open('alphaKey.txt', 'w')
#     for line in file_r:
#         temp = ''
#         for i in range(16):
#             temp += binary_map[line[i*4:i*4+4]]
#         file_w.write(temp + '\n')
#         print(temp)
#     file_r.close()
#     file_w.close()

# # def printNumericalvalue():
# #     file_r = open('binary64.txt')
# #     for line in file_r:
# #         temp = line.split('\n')[0]
# #         number = int(temp, 2)
# #         print(temp, number)
# #     file_r.close()
# # printNumericalvalue()
# generatePossibalAlphakey()