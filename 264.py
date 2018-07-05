class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1]
        p2, p3, p5 = 0, 0, 0
        while len(uglys) < n:
            ugly2, ugly3, ugly5 = uglys[p2] * 2, uglys[p3] * 3, uglys[p5] * 5
            min_ugly = min(ugly2, ugly3, ugly5)

            if ugly2 == min_ugly:
                p2 += 1
            if ugly3 == min_ugly:
                p3 += 1
            if ugly5 == min_ugly:
                p5 += 1
            if min_ugly != uglys[-1]:
                uglys.append(min_ugly)
        return uglys[-1]


print(Solution().nthUglyNumber(1))
