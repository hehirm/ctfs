import requests
from time import sleep
for i in range(1, 100):

    header = {'Cookie': f'name={i}'}
    sleep(0.2)
    response = requests.get('http://mercury.picoctf.net:29649/check', headers=header)
    if b'picoCTF{' in (response.content or response.headers):        
        print(response.content)
        print(response.headers)
        break
