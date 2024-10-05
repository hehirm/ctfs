# picoCTF2022 Secrets Write Up

## Description

> We have several pages hidden. Can you find the one with the flag? The website is running [here](http://saturn.picoctf.net:61549/).

## Solution

Looking at the data in the `<head>` tag of the target website reveals the following suspicious endpoint:

```
<link href="secret/assets/index.css" rel="stylesheet">
```

Navigating to the secret directory presents a new website indicating that this is the correct line of thinking
