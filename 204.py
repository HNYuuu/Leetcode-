import math
import datetime

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # com = [False] * (n+1) # assume all are primes
        # prime = []
        # primes = 0
        # i = 2
        # while i < n:
        #     if com[i] == False:
        #         prime.append(i)
        #         primes += 1
        #     j = 0
        #     while j < primes and i * prime[j] < n:
        #         com[i * prime[j]] = True
        #         j += 1
        #     i += 1
        # return primes
        prime = [True] * (n+1)
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if prime[i] == True:
                j = i*i
                while j <= n:
                    prime[j] = False
                    j += i
        return prime[2:-1].count(True)
            

start = datetime.datetime.now()
print(Solution().countPrimes(1500000))
end = datetime.datetime.now()
print(end - start)
