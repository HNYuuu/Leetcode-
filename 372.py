from functools import reduce


class Solution:
    def superPow(self, x, y):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        def quick_algorithm(a, b, c):
            a = a % c
            ans = 1
            while b != 0:
                if b & 1:
                    ans = (ans * a) % c
                b >>= 1
                a = (a * a) % c
            return ans

        # result = []
        # for i in range(len(y)):
        #     result.append(quick_algorithm(x, y[-i - 1] * (10 ** i), 1337))

        # return reduce(lambda x, y: (x * y) % 1337, result)
        return quick_algorithm(x, int(''.join([str(x) for x in y])), 1337)


print(Solution().superPow(2, [1, 0]))
