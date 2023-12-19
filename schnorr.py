# шнуруемся

import random

class SchnorrScheme:

    def __init__(self, primes : list[2]):
        """For constructor required [q, r] such that p = qr + 1, where p, q are primes, r is even"""
        
        self.q = primes[0]
        self.r = primes[1]

        h = 2
        self.p = self.q * self.r + 1
        # while (h ** self.r) % self.p == 1:
        #     h = random.randint(1, self.p - 1)
        while pow(h, self.r, self.p) == 1:
            h = random.randint(1, self.p - 1)

        #self.g = (h ** self.r) % self.p
        self.g = pow(h, self.r, self.p)

    def HASH(self, x : str, modulo : int):
        hash = 0
        for i in range(0, len(x)):
            hash += ord(x[i])
        return hash % modulo

class Message:

    def __init__(self, message, public_key):
        self.message = message
        self.public_key = public_key

    def sign(self, sig1, sig2):
        self.first_signature = sig1
        self.second_signature = sig2

    def get_signature(self):
        return (self.first_signature, self.second_signature, self.public_key)
    
    public_key = 0
    first_signature = 0
    second_signature = 0

class Agent:

    def generate_keys(self, grp : SchnorrScheme):

        self._private_key = random.randint(1, grp.q - 1)
        #self.public_key = (grp.g ** self._private_key) % grp.p
        self.public_key = pow(grp.g, self._private_key, grp.p)

    def get_public_key(self):
        return self.public_key

    def sign_message(self, msg : Message, grp : SchnorrScheme):
        """ requires a Scheme by which message will be signed """
        
        k = random.randint(1, grp.q - 1)

        #r = (grp.g ** k) % grp.p
        r = pow(grp.g, k, grp.p)

        print(f"Rs = {r}")

        sgn2 = grp.HASH(str(r) + str(msg.message), grp.q)
        sgn1 = (k - (self._private_key * sgn2)) % grp.q

        print(f"SIGNED:\n\tsgn1: {sgn1}\n\tsgn2: {sgn2}")

        msg.sign(sgn1, sgn2)

    def write_message(self, txt : str = "Hello, World!"):
        return Message(txt, self.public_key)
    
    def verify_message(self, msg : Message, grp : SchnorrScheme):

        sigs_w_key = msg.get_signature()
        sig1 = sigs_w_key[0]
        sig2 = sigs_w_key[1]
        public_key = sigs_w_key[2]
        #r = (((grp.g ** sig1) % grp.p) * ((public_key ** sig2) % grp.p)) % grp.p
        r = (pow(grp.g, sig1, grp.p) * pow(public_key, sig2, grp.p)) % grp.p
        e = grp.HASH(str(r) + str(msg.message), grp.q)
        print(f"Rr = {r}")
        if (sig2 == e):
            print("Verification successful!")
        else:
            print("Verification failed. Liar.")