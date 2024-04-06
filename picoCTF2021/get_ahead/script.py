import requests
response = requests.head('http://mercury.picoctf.net:34561/index.php');
print(response.headers)


