# PicoCTF2019 logon Write Up

## Description

> The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/15796/ (link) or http://jupiter.challenges.picoctf.org:15796 

## Solution

Initially navigating to the vulnerable website reveals a login page. Attempting to login with the default credentials `admin`, `admin` results in a successful login, although no flag. As per the challenge description, this is because we haven't logged in as the user Joe.

Comparing the site cookies before and after logging in reveals that there are three additional cookies after logging in:
-  `password`
- `username`
- `admin`

The last cookie is the most interesting. Using the above credentials, the `admin` cookie is set to `False`. Assuming that Joe is an admin, I attempted to set the value of this cookie to `True`. This resulted in the flag being displayed:

```
picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}
```


