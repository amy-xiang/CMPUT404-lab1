import requests

print("Python Requests Module Version: " + requests.__version__ )

print("--- \n")

response = requests.get('https://raw.githubusercontent.com/amy-xiang/CMPUT404-lab1/master/getRequestsVersion.py')

data = response.content.decode('utf-8')

print(data)



