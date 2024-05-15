# picoMini login Write Up

## Description

> My dog-sitter's brother made this website but I can't get in; can you help? [login.mars.picoctf.net](https://login.mars.picoctf.net)

## Solve

The page presents a basic login page, accepting a username and password. Trying the credential pair `admin`, `admin` produces an alert indicating the password is incorrect. The html for the page contains the following head information:

```html
<head>
	<link rel="stylesheet" href="styles.css">
	<script src="index.js"></script>
</head>
```

The page is loading some javascript code from a file called `index.js`. Going to `login.mars.picoctf.net/index.js` displays the contents of the javascript code:

```javascript
(async () => {
    await new Promise((e => window.addEventListener("load", e))), document.querySelector("form").addEventListener("submit", (e => {
        e.preventDefault();
        const r = {
                u: "input[name=username]",
                p: "input[name=password]"
            },
            t = {};
        for (const e in r) t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, "");
        return "YWRtaW4" !== t.u ? alert("Incorrect Username") : "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" !== t.p ? alert("Incorrect Password") : void alert(`Correct Password! Your flag is ${atob(t.p)}.`)
    }))
})();
```

The above code is performing the following actions when the user presses submit:
- The username and password are retrieved and stored in an object `r` with keys `u` for the username and `p` for the password.
- A new object `t` is created which contains the base64 encoded values of `r` with `=` characters removed.
- A ternary operator determines the message displayed. If the base64 encoded username (stored in `t.u`) is not equal to `YWRtaW4` then show the message `"Incorrect Username"`. `YWRtaW4` base64 decoded is `admin`. If the base64 encoded usernames match, then it checks whether the base64 encoded password (stored in `t.p`) is equal to `cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ`. If they don't match then the message shown is `"Incorrect Password"`, however if they do the message shown is `"Correct Password! Your flag is ` followed by the password entered. Thus the password is the flag. Base64 decoding `cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ` produces the password `picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}`.

The flag is:

```
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```