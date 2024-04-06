# picoCTF2021 GET aHEAD Write Up

## Description

> Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:34561/

## Solution

The site allows the user to switch between two themes: red and blue. Setting the colour to red is achieved by sending a GET request, and setting the colour to blue is achieved by sending a POST request. This behaviour struck me as odd, especially considering the capitalisation of GET within the title. Further, HEAD is also capitalised within the title and is also a valid HTTP request. We can send a HEAD request to the website using the following simple python script:

```python
import requests
response = requests.head('http://mercury.picoctf.net:34561/index.php');
print(response.headers)
```

This reveals the flag as:

```
picoCTF{r3j3ct_th3_du4l1ty_8f878508}
```
