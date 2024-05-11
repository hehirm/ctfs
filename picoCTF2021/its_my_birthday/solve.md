# picoCTF 2021 It is My Birthday Write Up

## Description

> I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. [http://mercury.picoctf.net:55343/](http://mercury.picoctf.net:55343/)

## Solve

Given the descriptions mention of matching md5 hashes and the titles reference to a birthday, I postulated that a Birthday Attack is going to be central to solving this challenge. One of the main properties that a hash function should possess is collision resistance i.e. producing two messages $M$ and $M'$ such that their hashes are the same ($H(M) = H(M')$) should be difficult. A birthday attack attempts to produce two such messages. The term birthday attack originates from the infamous [Birthday Problem](https://en.wikipedia.org/wiki/Birthday_problem) which explores the probability of any two individuals in a group sharing a birthday. Importantly, this probability is surprisingly high (a mere 23 individuals in the group results in the probability becoming greater than 0.5) making birthday attacks more difficult for hashing functions to defend against. The MD5 hash function has been proven to be susceptible to a birthday attack by Xiaoyun Wang and Hongbo Yu in their paper [How to break MD5 and Other Hash Functions](http://merlot.usc.edu/csac-f06/papers/Wang05a.pdf). In this paper they produce the following sequences of 128 bytes that produce the same hash:

```
d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89 
55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b 
d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0 
e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70
```

```
d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89 
55ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5b 
d8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0 
e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70
```

The hash these sequences produce is:

```
79054025255fb1a26e4bc422aef54eb4
```

This is half of the problem solved - the other half is storing these bytes within a PDF file such that the resulting hashes of the files are the same. Interestingly, the website is verifying the file type by the name of the extension. This can be validated by creating two files `file1.txt` and `file2.txt` with the contents `hello` and `world` respectively. Uploading these files as is produces an invalid file type error. However, changing the file extensions from `.txt` to `.pdf` results in an MD5 hash mismatch error, which confirms that the website now thinks that they are PDF files.

Putting everything together, we create two files called `file1.pdf` and `file2.pdf` and set the contents of these files to be the above byte sequences. Note that it is not sufficient to store these as the text contents of the files - we need the above sequences to be the byte contents of the files. The python script below does this:

```python
import binascii

with open("file1.pdf", "wb") as file1:
    contents = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
    contents = binascii.unhexlify(contents)
    file1.write(contents) 

with open("file2.pdf", "wb") as file2:
    contents = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"
    contents = binascii.unhexlify(contents)
    file2.write(contents) 
```

We can then upload the two files to the site, which produces the source code for the website that also contains the flag:

```
picoCTF{c0ngr4ts_u_r_1nv1t3d_aad886b9}
```