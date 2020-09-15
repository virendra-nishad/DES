from genText import*


input_set = ['f',   'g',   'h',   'i',   'j',   'k',   'l',  'm',    'n',   'o',  'p',   'q',   'r',   's',   't',   'u']
bit_set = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
plain = 'lkfkshhfumipknmf'
cipher = 'pjgorgoqtthiorgj'

plainBin = ''
cipheBin = ''
for i in range(len(plain)):
    plainBin += alphabet_map[plain[i]]
    cipheBin += alphabet_map[cipher[i]]
print(plainBin)
print(cipheBin)

for i in range(8):
    print(int(cipheBin[i*8:i*8+8], 2), ' ')