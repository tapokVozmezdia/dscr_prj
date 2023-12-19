import prime
import eratosthenes
import time
import math
import sys
import numpy as np
import schnorr

def mark():
    print("==================")

boundary = int(math.pow(2,20))

mySieve = eratosthenes.EratosthenesSieve(boundary)

s = time.time()
mySieve.sieve()
goodPrimes = mySieve.getPrimes()

primer = prime.Primer()

#print(primer.generatePrime(100))

"""fore some reason my schorr scheme doesn't work with primes 
that have above 25 digits in decimal form, probably some types
overwhelming, gonna fix later"""
pr = primer.get_prime(25, True)

print(pr)
s = time.time()
Scheme = schnorr.SchnorrScheme(pr)
(print(time.time() - s))

Alice = schnorr.Agent()
Bob = schnorr.Agent()
Charlie = schnorr.Agent()

Alice.generate_keys(Scheme)
Bob.generate_keys(Scheme)
Charlie.generate_keys(Scheme)

msg = Alice.write_message()
print(msg.get_signature())
Alice.sign_message(msg, Scheme)

print(msg.get_signature())

Bob.verify_message(msg, Scheme)
print(f"Message: {msg.message}\nHashed: {Scheme.HASH(msg.message, Scheme.q)}")