import math
import random
import eratosthenes

def euclidGcd(a, b):
    if b == 0:
        return a
    else:
        return euclidGcd(b, a % b)
    
def bruteForcePrimes(N):
    primes = []
    for num in range(2, N):
        flag = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            primes.append(num)
    return primes

class Primer:

    def __init__(self, scope = 1000):
        sieve = eratosthenes.EratosthenesSieve(scope)
        sieve.sieve()
        self.primes = sieve.getPrimes()

    def not_divisible_by_small_primes(self, n):
        for i in self.primes:
            if n % i == 0:
                return False
        return True

    def get_prime(self, n : int, decomposed : bool = False):
        """ 
        if decomposed flag is true, then returns [q, r], where qr + 1 = p, with q, p - primes;
        Generates prime number with at least n digits:

        : param n: number of 10-based digits in the generate prime is at least n;
        : param primes: an iterable object of numbers that are used as small factors
        for pre-prime verification. If None, is computed using getSieve(1000);
        : param s: initial prime number - if None, last from primes is used;
        """

        # Any prime number higher than the up_limit suffices the result.
        up_limit = 10**n

        # Get the list of small primes which are used as small divisors
        # to reject the n candidate before the Pocklington test.
        primes = self.primes

        s = primes[-1] # initial prime

        r = 1

        while s < up_limit:
            lo, hi = (s + 1) >> 1, (s << 1) + 1

            # Proceed with finding new prime n
            while True:
                r = random.randint(lo, hi) << 1 # get random even r from [s, 4*s + 2]
                n = s * r + 1 # n is prime candidate, s^2 + 1 <= n <= 4s^2 + 2s + 1

                # reject n if n divides some number in primes list
                if not self.not_divisible_by_small_primes(n): 
                    continue

                # Here n is probably prime - apply Pocklington criterion to verify it
                while True:
                    a = random.randint(2, n - 1)

                    # Fermat’s little theorem isn't satisfied - choose another n
                    if pow(a, n-1, n) != 1: 
                        break

                    d = math.gcd((pow(a, r, n) - 1) % n, n)
                    if d != n:
                        if d == 1: 
                            s = n # n is prime, replace s with n
                        else: 
                            pass # n isn't prime, choose another n
                        break
                    else: 
                        pass # a^r mod n == 1, choose another a
                if s == n: 
                    break
        if decomposed == False:
            return s
        else:
            return [int((s - 1) / r), int(r)]