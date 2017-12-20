# 给定四个数组, 从中分别取一个得到和为 0, 问有
# 几种方式. 二层遍历前两个数组, 把 a+b 作为 
# key, 有几个作为 value, 然后再遍历后两层, 
# 看 -c-d 在不在字典中, result += 取出的值即
# 可. 疯狂 TLE, 因为没有掌握正确的赋默认值方法

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        temp = {}
        for a in A:
            for b in B:
                temp[a+b] = temp.get(a+b, 0) + 1
        
        result = 0
        for c in C:
            for d in D:
                result += temp.get(0-c-d, 0)
        
        return result

print(Solution().fourSumCount())