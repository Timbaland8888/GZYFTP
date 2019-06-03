#!/usr/bin/python
#fuction:test wtc webapi chagevlan
import urllib.request
import json
import requests

data = {
    'vmIds': '4228d4cc-7ff9-7869-9ad5-cb66c5c0fe2c',
    'networkName': 'VLAN232'
}
values = urllib.parse.urlencode(data).encode(encoding='UTF8')
headers = {'Content-Type': 'application/json'}
url = 'http://192.168.128.61:8082/hj3-webapi/network/changeNetwork'
# print(data)
# print(values)
# print(json.dumps(data))
# print(json.dumps(data).encode())
# request = urllib.request.Request(url=url, headers=headers, data=json.dumps(data).encode(),method='POST')
# print(request.method)
# response = urllib.request.urlopen(request)
r = requests.post(url,data=json.dumps(data))
print(r.text)



