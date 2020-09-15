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

f = open('input.txt')
f2 = open('response.txt','w+')
data = '{"password":"f6e39f49461e278158f51a92e8ca0d84","teamname":"Obfuscated","plaintext":"password"}'
data = json.loads(data);
cipherTexts = []
count = 0
for line in f.readlines():
    data["plaintext"] = line.split('\n')[0]
    r = requests.post(url, json=data, headers=headers, verify=False)
    if(r.status_code == 200):
        response = json.loads(r.text)
        print(response)
        print(count)
        count+=1
        cipherPlain = "{0}\n".format(response["ciphertext"])
        f2.write(cipherPlain)
    else:
        print("Failed")
f.close()

# print(cipherTexts[0])

# r = open('Responsefile.txt','w')
# r.writelines(cipherTexts)
f2.close()
applyAntiFinalPerm()