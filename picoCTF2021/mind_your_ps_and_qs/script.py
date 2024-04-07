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


