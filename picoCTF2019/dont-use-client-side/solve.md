# PicoCTF2019 dont-use-client-side Write Up

## Description

> Can you break into this super secure portal? `https://jupiter.challenges.picoctf.org/problem/29835/` ([link](https://jupiter.challenges.picoctf.org/problem/29835/)) or http://jupiter.challenges.picoctf.org:29835

## Solve

Opening up the website reveals a credential verifier. The challenge name suggests that verification of these credentials is occurring on the client side. Checking the source code for the website confirms this - we can find the following script in the source code:

```
<script type="text/javascript">
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == '723c') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_7') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == 'e}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
    
  }
</script>
```

The script is verifying the credentials in lots of four characters, also out of order. Piecing the substrings begin checked against in the correct order results in the following string:

```
picoCTF{no_clients_plz_7723ce}
```

This is not only a valid credential to the site, but also the flag.