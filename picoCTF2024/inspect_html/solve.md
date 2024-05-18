# picoCTF2024 Inspect HTML Write Up

## Description

> Can you get the flag? Go to this [website](http://saturn.picoctf.net:58599/) and see what you can discover.

## Solution

The flag is contained within a HTML comment on the target website:

```
<!--picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}-->
```

Thus the flag is:

```
picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}
```