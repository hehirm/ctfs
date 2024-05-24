# picoCTF2021 Some Assembly Required Write Up

## Description

> http://mercury.picoctf.net:36152/index.html

## Solution

Looking at the network traffic there are three GET requests being performed:

- One to fetch the `index.html` page
- One to fetch a a Javascript file called `G82XCw5CX3.js` which contains obfuscated Javascript code
- One to fetch a file called `JIFxzHyW8W` which is a binary file

Within the last file, there is a string that is reminiscent of a picoCTF flag:

```
picoCTF{d88090e679c48f3945fcaa6a7d6d70c5}
```

This is in fact the flag for the challenge

