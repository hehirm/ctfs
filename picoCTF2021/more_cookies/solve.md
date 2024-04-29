# PicoCTF2021 More Cookies Write Up

## Description

> I forgot Cookies can Be modified Client-side, so now I decided to encrypt them! [http://mercury.picoctf.net:34962/](http://mercury.picoctf.net:34962/)

## Solution

The page displays the message:

> Welcome to my cookie search page. Only the admin can use it!

Meaning that the goal here is to become an admin. Noting the absence of any kind of login functionality, this must be determined by a session token.

Looking at my cookies, there is a session token with name `auth_name` and value set to:

```
NnlNWmd3Mm45bm1odmcyb0pxcWtLK00zenk2OUd2aWoyN3lsWUZycU93OTlYQTBxcXNyV25Fa0ZVdnFGUWtJQzk3WU1OMFpab0c5WjVyM0h0QWdNNU5zQ0NIT095NnJlSzVjL0hucmNmdnVCa2JOUkp4ZjY0SkQvYXV4elNzNEU=
```

This looks like a base64 encoded string. Attempting to decode it produces nothing to work with as the challenge states that the cookies are encrypted. After trying multiple different approaches to determine the encryption method being used I consulted some write ups indicated that the encryption method being used is Cipher Block Chaining (PicoCTF just *loves* to hide hidden details in the challenge description).

With this information I began acquainting my self with block ciphers and cipher block chaining. I cam across [this](https://alicegg.tech/2019/06/23/aes-cbc) article which describes why CBC is vulnerable to a bit flip attack. 




Flag:

## Aside: Block Ciphers and Cipher Block Chaining

Here I go into a little more depth about why bit flipping is an appropriate attack strategy. My understanding of this topic to a large extent comes from [this](https://alicegg.tech/2019/06/23/aes-cbc) article (I would recommend reading it over my hacky explanation).

### Block Ciphers

Like all ciphers, a block cipher is made up of two algorithms: one for encryption and one for decryption. What differentiates a block cipher from other kinds, is that the encryption and decryption algorithms can only act on inputs of a very particular size. These inputs are called *blocks*. 

The encryption algorithm accepts a plaintext block of the required size as well as an encryption key and produces a ciphertext block *of the same size*. The decryption algorithm performs the input operation, accepting a ciphertext block and key to produce a plaintext block.

One of the most common block ciphers is AES. AES-256 uses a 128 bit block size and a 256 bit key. 

An tangential note here is that a block cipher essentially spits out a permutation of the input block according to the algorithm used and the secret key. The number of permutations is $2^n$ where $n$ is the block size in bits. This explains why for AES we can have a key that is larger than the block size - the key is responsible for mapping permutations which are much larger than the block size itself.

## Cipher Block Chaining

Block ciphers are useless on their own as they can't encrypt anything larger than their block size. To encrypt larger data we need a *block cipher mode of operation*, which specifies how to break a larger piece of data into blocks that are repeatedly passed through the block cipher algorithms in a way that is cryptographically secure.

A naive way to do this for encryption is to split a piece of plaintext into blocks of the correct size, apply the block cipher encryption algorithm to each block and then join the resulting ciphertext blocks together. This naive approach comes with the added benefit that the decryption process is essentially identical, save the use of the block cipher decryption algorithm. This mode of operation is commonly referred to as **Electronic codebook (ECB)**. This mode is highly insecure, as identical plaintext blocks get turned into identical ciphertext blocks i.e. there is a lack of diffusion (go read the wikipedia article on this, the images explain why this is an issue quite nicely).

**Cipher Block Chaining (CBC)** came along to address this diffusion issue. The main idea is that before encrypting a plaintext block it is XORed with the encrypted ciphertext of the previous block before being encrypted. The following graphic makes this clear:

- TODO insert graphic

Decryption works in a similar way. 