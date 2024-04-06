# picoCTF2019 where are the robots Write Up

## Description

> Can you find the robots? https://jupiter.challenges.picoctf.org/problem/60915/ (link) or http://jupiter.challenges.picoctf.org:60915

## Solution

The presence of robots in the challenge description indicates checking the `robots.txt` file. Checking this file reveals a disallow endpoint for the endpoint `/8028f.html`

```
User-agent: *
Disallow: /8028f.html
```

Going to this endpoint reveals the flag:

```
picoCTF{ca1cu1at1ng_Mach1n3s_8028f}
```

