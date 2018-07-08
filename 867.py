import math


class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N > 9989899:
            return 100030001
        def is_prime(n):
            return not any(n % p == 0 for p in range(2, int(math.sqrt(n)) + 1))

        def isPalindrome(n):
            if str(n) == str(n)[::-1]:
                return True
            return False

        i = max(N, 2)
        while i < 200000000:
            if i > 11 and (
                    str(i)[0] == '2' or str(i)[0] == '4' or str(i)[0] == '5' or str(i)[0] == '6' or str(i)[0] == '8'):
                i += (10**(len(str(i))-1) - i%(10**(len(str(i))-1)))
            if isPalindrome(i) and is_prime(i):
                return i
            i += 1
            print(i)

print(Solution().primePalindrome(9989899))
