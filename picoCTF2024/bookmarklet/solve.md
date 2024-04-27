# PicoCTF2024 Bookmarklet Write Up

## Description

> Why search for the flag when I can make a bookmarklet to print it for me? Browse here, and find the flag! 

## Solution

Going to the site url, the site generates some Bookmarklet code that contains the flag:

```
javascript:(function() {
    var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÉÕËÆÒÇÚËí";
    var key = "picoctf";
    var decryptedFlag = "";
    for (var i = 0; i < encryptedFlag.length; i++) {
        decryptedFlag += String.fromCharCode((
	        encryptedFlag.charCodeAt(i) - key.charCodeAt(
		        i % key.length) + 256) % 256
		);
    }
    alert(decryptedFlag);
})();
    
```

Specifically, this code should decrypt the encrypted flag and produce an alert with its contents.

To run the bookmarklet, create a new book mark and use the above script as the URL. Accessing the bookmark then displays the flag:

```
picoCTF{p@g3_turn3r_cebccdfe}
```


