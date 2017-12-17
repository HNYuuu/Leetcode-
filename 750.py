# 给定一个二维数组，计算可以围成矩形的个数。这道题当时废了
# 一点功夫，最后想到如果可以围成一个矩形，那么那两行做与
# 运算两个角一定为1，剩下的一定为0，如果有不止两个1，那么
# 用C(n,2)即可

class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        vertical = len(grid)
        horizontal = len(grid[0])

        def grid2int(grid, line):
            result = []
            for i in grid[line]:
                result.append(str(i))
            temp = "".join(result)
            return int(temp, 2)

        def countbit(num):
            temp = bin(num)[2:]
            return temp.count('1')

        count = 0
        bitmap = [-1] * (vertical)
        for i in range(0, vertical):
            for j in range(i+1, vertical):
                if bitmap[i] != -1:
                    bit1 = bitmap[i]
                else:
                    bit1 = grid2int(grid, i)
                    bitmap[i] = bit1
                if bitmap[j] != -1:
                    bit2 = bitmap[j]
                else:
                    bit2 = grid2int(grid, j)
                    bitmap[j] = bit2
                result = bit1 & bit2
                bit1count = countbit(result)
                if bit1count == 0:
                    continue
                else:
                    count += (bit1count*(bit1count-1))//2
        return count

print(Solution().countCornerRectangles([[1, 1, 1]]))
