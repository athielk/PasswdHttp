import requests
import requests
import os
import urllib
myurl = 'http://localhost:8000'
print("here")
# response = requests.get(myurl+"/users")
# print(response.text)
# response = requests.get(myurl+"/users/query", 'shell=%2Fbin%2Ffalse')
# print(response.text)
response = requests.get(myurl+"/groups/query", 'member=_analyticsd&member=_networkd')
print(response.text)
# response = requests.get(myurl)
# print(response)