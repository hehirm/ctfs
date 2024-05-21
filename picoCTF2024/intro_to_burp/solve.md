# picoCTF2024 IntroToBurp Write Up

## Description

> Try [here](http://titan.picoctf.net:60722/) to find the flag

## Solution

The site presents a simple sign up with multiple inputs for a form. Filling in these details and submitting the form initiates a POST request that redirects to the `/dashboard` endpoint. This endpoint requires the user to input a One Time Passcode (OTP). Submitting an arbitrary OTP value sends a POST request with the value to the server and yields an `Invalid OTP` message.

One of the challenge hints suggests trying to mangle the HTTP requests in an attempt to interfere with the backend code. As a starting point, I tried removing the OTP field from the second POST request. To my surprise, this was sufficient to obtain the flag:

```
picoCTF{#0TP_Bypvss_SuCc3$S_9090d63c}
```
