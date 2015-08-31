'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''


class L204_Count_Primes_Ezy:
    
    # @param {integer} n
    # @return {integer}
    
    # sieve of eratosthenes
    def countPrimes(self, n):
        if n < 2:
            return 0
        seive = [True] * n
        seive[0] = False
        seive[1] = False
        i = 2
        while i * i < n:
            if seive[i]:
                j = i
                while i * j < n:
                    seive[i * j] = False
                    j += 1
            i += 1
        return sum(seive)