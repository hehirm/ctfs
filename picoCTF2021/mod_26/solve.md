# picoCTF2021 Mod 26 Write Up

## Description

> Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}

## Solution

The challenge provides what seems to be an encoded flag. It also makes reference to ROT13, which is essentially a caesar cipher with a key of 13. This means that encoding a string with ROT13 twice yields a total shift of 26 i.e. the decoded text. Passing the encoded text through a ROT13 encoder (I used [cyberchef](https://gchq.github.io/CyberChef/)) reveals the flag:

```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}
```
