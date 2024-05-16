# picoCTF2024 Includes Write Up

## Description

> Can you get the flag? Go to this [website](http://saturn.picoctf.net:62084/) and see what you can discover.

## Solution

The target website contains the following information about include directives:

> Many programming languages and other computer files have a directive, often called include (sometimes copy or import), that causes the contents of a second file to be inserted into the original file. These included files are called copybooks or header files. They are often used to define the physical layout of program data, pieces of procedural code and/or forward declarations while promoting encapsulation and the reuse of code.

Web applications often require the use of separate files to add styling/additional functionality to the website. Two basic examples of this are `.css` and `.js` files. Given the similarity to include directives in programming languages, these files will be suitable candidates for exploration in this challenge.

The `<head>` tag of the main page links to a `style.css` file. This file contains the following contents:

```css
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```

The last line contains the first part of a flag. It also indicates that it is the first of two pieces. The second piece is likely included in another file.

Looking at the `<body>` tag of the main page, we can see that it links to a `script.js` file. This file contains the following contents:

```javascript
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_6edef411}
```

The last line contains the second part of the flag. Putting the two pieces together produces the flag:

```
picoCTF{1nclu51v17y_1of2_f7w_2of2_6edef411}
```

