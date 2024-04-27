# PicoCTF2024 WebDecode Write Up

## Description

> Do you know how to use the web inspector? Start searching here to find the flag 

## Solution

The application has three webpages:
- Home, at the endpoint `index.html`
- About, at the endpoint `about.html`
- Contact, at the endpoint `contact.html`

The description makes reference to the web inspector, so the source contents are going to be the most likely places for these flags.

Looking at the html for the About page, we can see the following element:

```html
<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9">
   <h1>
    Try inspecting the page!! You might find it there
   </h1>
   <!-- .about-container -->
  </section>
```

The `notify_true` attribute contains what appears to be a base64 encoded string. Running the string through a base64 decoder produces the flag:

```
picoCTF{web_succ3ssfully_d3c0ded_df0da727}
```
