# picoCTF2021 Scavenger Hunt Write Up

## Description

> There is some interesting information hidden around this site http://mercury.picoctf.net:39698/. Can you find it?

## Solution

This challenge is very similar to the picoCTF2019 Insp3ct0r challenge. Inspecting the HTML source code revealed the first part of the flag:

```html
<!-- Here's the first part of the flag: picoCTF{t-->
```

Using my knowledge from the previous CTF I then checked out the CSS and Javascript files too (end points `mycss.css` and `myjs.js` respectively), which gave another part of the flag and a hint to the location of the third part:

```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

```js
/* How can I keep Google from indexing my website? */
```

The way to prevent google from indexing a website is by defining a disallow rule in the `robots.txt` endpoint. The `robots.txt` file contains another flag piece, as well as a hint for the next piece:

```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

The capitalisation of access and the mention of an apache server within this clue point to the `.htaccess` endpoint. This endpoint provides another flag piece as well as a clue to find the final piece:

```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

The macOS operating system uses a .DS_Store file within every directory to store custom attributes of its containing folder. The .DS_Store endpoint contains the final flag piece:

```
Congrats! You completed the scavenger hunt. Part 5: _fa04427c}
```

Putting all the pieces together produces the flag:

```
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_fa04427c}
```


