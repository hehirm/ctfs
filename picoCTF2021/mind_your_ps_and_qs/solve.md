# picoCTF2021 Mind your Ps and Qs Write Up

## Description

> In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values

The challenge includes a file an encrypted ciphertext as well as the values for n and e used in the encryption.

```
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537
```

## Solution

The challenge refers to RSA, so n and e are the encryption modulus and exponent respectively. If n is small enough that the factors can be found, then the cryptosystem can be broken. The value for n is small, but large enough that finding its factors using brute force will take too long. However, it can be compared against a database of known factorisations. Using [factordb](http://www.factordb.com/) the factors were found to be:

```
p: 1955175890537890492055221842734816092141
q: 670577792467509699665091201633524389157003
```

Using these values, we can compute the Euler Totient function of n, defined as:

$$
\varphi(n) = (p - 1) \times (q - 1)
$$

The decryption key/exponent can be calculated as:

$$
d = e^{-1} \ \text{mod} \ \varphi(n)
$$

Finally, the decrypted message can be computed as:

$$
m = c^d \ \text{mod} \ n
$$

The python script below accomplishes this (with the additional conversion of the decrypted number to a string):

```
import math
import gmpy2
from factordb.factordb import FactorDB

#Provided data
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423

# Factors of n
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003

# Different way of getting p and q using the factordb python interface
# f = FactorDB(n)
# f.connect()
# p, q = f.get_factor_list()


# Calculate Eulers totient of n
euler_phi = (p - 1) * (q - 1)

# Calculate the decryption key
d = gmpy2.invert(e, euler_phi)

# Decrypt the message
plaintext = gmpy2.powmod(c, d, n)

# Convert the message into a string
plaintext = bytes.fromhex(hex(plaintext).lstrip("0x")).decode()

print(f"Flag: {plaintext}")
```

Running the above script produces the flag:

```
picoCTF{sma11_N_n0_g0od_13686679}
```





