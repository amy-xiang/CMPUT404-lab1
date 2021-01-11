import requests

print(requests.__version__)

x = requests.get('https://www.google.com/')

print(x.content)

