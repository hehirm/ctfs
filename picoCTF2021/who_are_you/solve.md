# picoCTF2021 Who are you? Write Up

## Description

> Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn [http://mercury.picoctf.net:46199/](http://mercury.picoctf.net:46199/)

## Solve

This challenge is primarily an exercise in exploring different HTTP headers. The default GET request used to load the page is:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:46199
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

We will iteratively update the format of this request as required.

The website initially displays the following message:

> Only people who use the official PicoBrowser are allowed on this site!

The browser being used is handled by the `User-Agent` header (this header handles other things too). Observe that in the default request, the browser is set to Mozilla Firefox (my browser). We can thus modify this header to have the contents `PicoBrowser`. The new request is:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:46199
User-Agent: PicoBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

Sending this request off now produces a different message:

> I don't trust users visiting from another site.

The referring site is handled by the `Referer` header. It is absent from the default request, but we can explicitly set it to the domain of the challenge website. The updated request is then:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:46199
User-Agent: PicoBrowser
Referer: http://mercury.picoctf.net:46199/
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

Sending this new request off again produces a new message:

> Sorry, this site only worked in 2018.

We can specify the date of a message (in this case a GET request) with the `Date` header. Any value in 2018 will do. The updated request now looks like:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:46199
User-Agent: PicoBrowser
Referer: http://mercury.picoctf.net:46199/
Date: Mon, 07 Feb 2018 00:28:05 GMT
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

Sending off this request again produces a new message:

> I don't trust users who can be tracked.

Tracking is handled by the `DNT` header (stands for Do Not Track). This header can take on three values:
- 0: Indicates that the user wants to be tracked
- 1: Indicates that the user does not want to be tracked
- null: Indicates that the user has no tracking preferences

We thus set the value to 1. The new request looks like:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:46199
User-Agent: PicoBrowser
Referer: http://mercury.picoctf.net:46199/
Date: Mon, 07 Feb 2018 00:28:05 GMT
DNT: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

Sending this request produces a new message:

> This website is only for people from Sweden.

This one is a little more tricky. If a user sends a request directly to the server, the clients IP address is used in the IP protocol. However, if the request is sent through a proxy, then the original IP address is replaced with the IP of the outgoing interface of the proxy. Often the sending IP address is needed. This is what the `X-Forwarded-For` header is used for (this is now depreciated in lieu of the `Forwarded` header). We can set this header to any IP address from Sweden. The new request becomes:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:46199
User-Agent: PicoBrowser
Referer: http://mercury.picoctf.net:46199/
Date: Mon, 07 Feb 2018 00:28:05 GMT
DNT: 1
X-Forwarded-For: 102.177.146.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

Sending this request produces a new message:

> You're in Sweden but you don't speak Swedish?

We need to set the Swedish language in the request. This can be done with the `Accept-Language` header. This header is already in the request - we only need to add the country code for Sweden which is `sv`. The request becomes:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:46199
User-Agent: PicoBrowser
Referer: http://mercury.picoctf.net:46199/
Date: Mon, 07 Feb 2018 00:28:05 GMT
DNT: 1
X-Forwarded-For: 102.177.146.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en,sv;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

Sending this last request off produces the flag:

```
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_8d5d8d77}
```



