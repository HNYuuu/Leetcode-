# 给定一堆区间, 找到最小的数可以穿过这些区间. 使用贪心的
# 算法, 将区间的开始作为 key 排序, 找到第一个区间, 然后
# 向后遍历, 注意截止处是在当前区间的终点和一开始区间的终
# 点取最小值

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x:x[0])
        i = 0
        result = 0
        while i < len(points):
            start = points[i][0]
            end = points[i][1]
            shoot = 1
            for j in range(i+1, len(points)):
                if points[j][0] <= end:
                    shoot += 1
                    end = min(points[j][1], end)
                else:
                    break
            result += 1
            i += shoot
        return result

print(Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))