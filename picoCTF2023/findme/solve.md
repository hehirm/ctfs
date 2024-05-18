# picoCTF2023 findme Write Up

## Description

> Help us test the form by submiting the username as `test` and password as `test!` The website running [here](http://saturn.picoctf.net:51253/).

## Solution

The website presents a simple login form, accepting a username and password. As per the websites direction, I used the login credentials `test`, `test!`. This results in a webpage with a search bar intended for flags. Attempting to use the search bar does not produce any results. The source code claims that a search queries the server - although as far as I could tell this is not the case.

Interestingly, before landing on the search page the login request makes two redirects: one to `/next-page/id=cGljb0NURntwcm94aWVzX2Fs` and the other to `/next-page/id=bF90aGVfd2F5X2JlNzE2ZDhlfQ==`. The id components of these subdirectories appear to be base64 encoded strings. Decoding these produces the following strings:

```
picoCTF{proxies_al
l_the_way_be716d8e}
```

Putting these two strings together produces the flag:

```
picoCTF{proxies_all_the_way_be716d8e}
```
