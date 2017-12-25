# 找到一个递增二维数组的第k小的元素. 既然是递增
# 的, 说明把每行合并用快排不会出现最坏情况, 根
# 据下标返回即可. 还可以用小根堆, pop(0)直到出
# 来k个元素, 但是容易超时, 这道题可以将某一列
# 或行作为一个堆, 记录坐标, 弹出后将其相邻的那
# 个推入进行调整

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        result = []
        for row in matrix:
            result.extend(row)
        result.sort()
        return result[k-1]

for i in range(1,26):
    print(Solution().kthSmallest([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], i))