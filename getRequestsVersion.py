import requests

# Referenced alko (November 24, 2013) on StackOverflow: https://stackoverflow.com/questions/20180543/how-to-check-version-of-python-modules
print("Python Requests Module Version: " + requests.__version__ )

print("--- \n")

# Referenced FlyingV (May 18, 2020) on StackOverflow: https://stackoverflow.com/questions/23049767/parsing-http-response-in-python 
response = requests.get('https://raw.githubusercontent.com/amy-xiang/CMPUT404-lab1/master/getRequestsVersion.py')
data = response.content.decode('utf-8')

print(data)



