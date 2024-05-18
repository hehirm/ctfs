# picoCTF2022 Search Source Write Up

## Description

> The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is [here](http://saturn.picoctf.net:50687/)

## Solution

This challenge is similar to previous challenges that require the solver to find artefacts hidden in the source code. The difficulty of this challenge comes from the significant content increase for the site. The site is spread across multiple source files meaning there are more independent places to look. Also each file contains more data meaning the chances of missing a critical piece of information are significantly increased.

To this end, a more optimised search strategy is required to obtain the flag. The following strategies were helpful in solving this challenge:

- Prioritisation of files to check. Consider the files `custom.js` and `jquery-3.0.0.min.js`. Between these two files, my money would be on `custom.js` to contain the flag. The latter file is likely not created by the site author meaning less likelihood that it has been modified to contain the flag. Note that this not a guarantee, but it is helpful in determining which files to check first.
- Automatic searching of files. Instead visual examination of files, it is better to use an automatic searching tool for the content of interest. In this case, we know that the flag structure is of the form `picoCTF{some_content}`, so we can search for `picoCTF`. Most browsers (can confirm for FireFox at the very least) will have functionality within their source code inspection tools to search for particular strings. It is typically accessed via Ctrl/Cmd + f.

Using these tools, I was able to find the flag in the `style.css` file (in the `css` directory):

```
picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}
```

