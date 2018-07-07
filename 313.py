class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglys = [1]
        ps = [0 for _ in range(len(primes))]

        while len(uglys) < n:
            temp = []
            for p in range(len(primes)):
                temp.append(uglys[ps[p]]*primes[p])
            min_ugly = min(temp)
            for i in range(len(temp)):
                if min_ugly == temp[i]:
                    ps[i] += 1
            if min_ugly != uglys[-1]:
                uglys.append(min_ugly)

        return uglys[-1]

print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))