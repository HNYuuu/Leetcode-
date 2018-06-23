import math

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        flag = [0 for _ in range(n+1)]

        def find_k_min(x):
            count = 0
            for i in range(1, len(flag)):
                if flag[i] == 1:
                    continue
                elif count < x:
                    count += 1
                else:
                    flag[i] = 1
                    return i

        result = ''

        while n > 0:
            x = k//(math.factorial(n-1))
            result += str(find_k_min(x))
            k = k%math.factorial(n-1)
            n -= 1

        return result

print(Solution().getPermutation(1,1))