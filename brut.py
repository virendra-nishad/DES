import requests
import json
import warnings
from IOprocessing import *

# prepare a random text file before running it
# and then apply anti permutation in order to cancel permutation

warnings.filterwarnings('ignore')
url = "https://172.27.26.181:9999/des"
headers = {'Content-type':'application/json',
             'Orgin': 'https://172.27.26.181:9999',
             'Referer':'https://172.27.26.181:9999/game/caves.swf'}

f = open('alphaKey.txt')
f2 = open('jasonData.txt','w+')
data = '{"password":"f6e39f49461e278158f51a92e8ca0d84","teamname":"Obfuscated","plaintext":"password"}'
data = json.loads(data);
cipherTexts = []
count = 0
true_key_set = set()
for line in f.readlines():
    data["plaintext"] = line.split('\n')[0]
    r = requests.post(url, json=data, headers=headers, verify=False)
    if(r.status_code == 200):
        response = json.loads(r.text)
        #f2.write(response)
        print(response)
        print(count)
        count+=1
        cipherPlain = "{0}\n".format(response["ciphertext"])
        success = "{0}\n".format(response["success"])
        success = success.split('\n')[0]
        if success == 'True':
            temp = line.split('\n')[0] + ':' + cipherPlain.split('\n')[0]
            true_key_set.add(temp)
        cipherPlain = cipherPlain.split('\n')[0]
        print(count, cipherPlain + ':' + success)
        f2.write(cipherPlain + ':' + success + '\n')
    else:
        print("Failed")
    print(true_key_set)
for item in true_key_set:
    f2.write(item + '\n')
f2.close()
f.close()

# print(cipherTexts[0])

# r = open('Responsefile.txt','w')
# r.writelines(cipherTexts)
f2.close()
applyAntiFinalPerm()