# 给定一个二维数组, 代表一面砖墙, 找到一个分界线可以打断
# 最少的砖, 不可以是两边. 这道题我干想是想不出来的, 看了
# 一下 related topic 发现是 hash table, 于是就联想到
# 了那道判断三个点是不是对称的那道题, 觉得可以把到某个距
# 离有空隙作为 key, 个数作为 value, 最后找 value 的最
# 大值, 用砖墙的高度减去即可

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        distanceCnt = {}
        for row in wall:
            distance = 0
            for length in row:
                distance += length
                distanceCnt[distance] = distanceCnt.get(distance, 0) + 1
        if len(distanceCnt) == 1:
            return len(wall)
        distanceCnt.pop(max(distanceCnt.keys()))
        space = max(distanceCnt.values())
        return len(wall)-space

print(Solution().leastBricks([[1],[1],[1]]))

