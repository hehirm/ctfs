# picoCTF2022 Local Authority Write Up

## Description

> Can you get the flag? Go to this [website](http://saturn.picoctf.net:60384/) and see what you can discover.

## Solution

The website is a customer portal containing fields to enter a username and password. On an attempt to login, a POST request is sent to `login.php` containing the login credentials. The request responds with a HTML page containing some client side scripts used for authentication. Attempting to login with the credentials `adim`, `admin` produces the following HTML page:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Login Page</title>
  </head>
  <body>
    <script src="secure.js"></script>
    
    <p id='msg'></p>
    
    <form hidden action="admin.php" method="post" id="hiddenAdminForm">
      <input type="text" name="hash" required id="adminFormHash">
    </form>
    
    <script type="text/javascript">
      function filter(string) {
        filterPassed = true;
        for (let i =0; i < string.length; i++){
          cc = string.charCodeAt(i);
          
          if ( (cc >= 48 && cc <= 57) ||
               (cc >= 65 && cc <= 90) ||
               (cc >= 97 && cc <= 122) )
          {
            filterPassed = true;     
          }
          else
          {
            return false;
          }
        }
        
        return true;
      }
    
      window.username = "admin";
      window.password = "admin";
      
      usernameFilterPassed = filter(window.username);
      passwordFilterPassed = filter(window.password);
      
      if ( usernameFilterPassed && passwordFilterPassed ) {
      
        loggedIn = checkPassword(window.username, window.password);
        
        if(loggedIn)
        {
          document.getElementById('msg').innerHTML = "Log In Successful";
          document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
          document.getElementById('hiddenAdminForm').submit();
        }
        else
        {
          document.getElementById('msg').innerHTML = "Log In Failed";
        }
      }
      else {
        document.getElementById('msg').innerHTML = "Illegal character in username or password."
      }
    </script>
    
  </body>
</html>
```

Of interest here is the contents of the final script tag. Within this tag a `filter` function is defined, which takes in a string and returns true or false depending on whether the string contains any non-alphanumeric characters. 

After this filter function is the preamble to the authentication logic. It first sets the `window.username` and `window.password` variables to the values we passed in on the login page. These values are then passed through the filter function, with the results stored in `usernameFilterPassed` and `passwordFilterPassed`. 

Finally comes the authentication logic itself. It first checks that both `usernameFilterPassed` and `passwordFilterPassed` are both true i.e. both the username and password contain only alphanumeric characters. If this condition is not satisfied, the paragraph tag with id `msg` is set to "Illegal character in username or password". If the filtering checks pass, the logic then calls the `checkPassword` function, storing the result in the variable `loggedIn`.  The next conditional statement seems to check if `loggedIn` is true - so it is reasonable to assume that `checkPassword` returns a boolean (true if authentication succeeds and false otherwise). If `loggedIn` is false, the `msg` paragraph tag is set to "Log In Failed". By contrast, if it is true, the the tag is set to "Log In Successful". Additionally, if the login is successful, the script sets the input `adminFormHash` for the form `hiddenAdminForm` to the hashed value `2196812e91c29df34f5e217cfd639881`. It then submits this form, making a POST request to  `admin.php`. This hash value is (at this stage presumable) used to get the flag.

The main piece missing from the above logic is the details of the `checkPassword` function. It is not defined within the script in the same way the `filter` function is. However, at the start of the documents body, there is a script tag that imports a javascript file called `secure.js`. This file has the following contents:

```javascript
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

This file contains the `checkPassword` function! The password returns true if the username is set to `admin` and the password is set to `strongPassword098765` and false otherwise. Since we want the function to return true (as per the authentication logic) the login credentials must be `admin`, `strongPassword098765`. Using these as the inputs to the portal produces the flag:

```
picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}
```
