import requests
import sys

response = requests.get(f'http://caas.mars.picoctf.net/cowsay/{sys.argv[1]}')
print(response.text)
