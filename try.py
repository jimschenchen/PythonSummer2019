from urllib.request import urlopen
import json
import requests

'''
with open('jim.txt') as fo:
    for line in fo:
        print(line.rstrip())
    
with open('jim.txt', 'a') as fo:
    fo.write('xixi')
'''

'''
json_url = 'http://www.probejfury.com/btc_close_2017.json'
response = urlopen(json_url)

req = response.read()

with open('btc.json', 'wb') as f:
    f.write(req)

print(req)
#file_urllib = json.loads(req)
#print(file_urllib)
'''

json_url = 'http://www.probejfury.com/btc_close_2017.json'
req = requests.get(json_url)
file_requests = req.json()
print(req)
print(file_requests)