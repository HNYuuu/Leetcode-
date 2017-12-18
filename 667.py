# 给定两个参数，找到符合这两个参数的list。先找出 k=n-1 
# 时的情况，一定是 [1,n,2,n-1,...]，于是可以根据这个
# 构造 k 是任意情况时的 list。只需要先按照此规律排列 k 
# 个数字，剩下的按照当时的尾数直接升序或降序补充即可

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        a = 1
        b = n
        count = 0
        result = []
        while True:
            result.append(a)
            count += 1
            a += 1
            if count == k:
                break
            result.append(b)
            count += 1
            b -= 1
            if count == k:
                break
        if result[k-1] > n//2:
            result.extend([i for i in range(b, a-1, -1)])
        else:
            result.extend([i for i in range(a, b+1)])
        return result

print(Solution().constructArray(3,2))
