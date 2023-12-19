import math

class EratosthenesSieve:
    
    def __init__(self, sieve_size = 100):

        self.sieve_size = sieve_size
        self.found_primes = []

    def sieve(self):
        nums = [False, False]
        for i in range(2, self.sieve_size + 1):
            nums.append(True)
        p = 2
        while True:
            if p * p >= self.sieve_size:
                break
            p1 = p * p

            while (p1 < len(nums)):
                nums[p1] = False
                p1 += p

            p += 1
        for i in range(0, len(nums)):
            if nums[i]:
                self.found_primes.append(i)
        
    def getPrimes(self):
        return self.found_primes