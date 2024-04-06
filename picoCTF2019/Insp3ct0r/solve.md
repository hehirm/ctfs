# picoCTF2019 Insp3ct0r Write Up

## Description

> Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/44924/ (link) or http://jupiter.challenges.picoctf.org:44924

## Solve

Exploring the website html source revealed the following comment:

```html
<!--  Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

Thus there are two other parts that are required for the flag. The website makes note of the three things they used to make the site: HTML, CSS and Javascript. We've looked at the HTML, so we should probably look at the other two.

The CSS is located at the endpoint `/problem/44924/mycss.css` (this information can be found in the HTML `<head>` tag). Inspecting the CSS reveals the second part of the flag:

```css
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

Finally lets have a look at the Javascript, which is located at the endpoint `/problem/44924/mycss.css`. Again, within the Javascript is a comment containing the last part of the flag:

```js
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?f10be399} */
```

Putting all the three pieces together:

```
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}
```
