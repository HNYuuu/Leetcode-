# 给定一个list，找到离每一个元素最近的较大值的索引差。这道题可
# 以用栈结构来解，如果压入的值比栈顶大，那么弹出栈顶，继续比较，
# 直到栈顶大于等于压入值，将其压入。每一个温度需要记录其索引值，
# 方便后续的填入索引差。

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * (len(temperatures))
        index = 0
        temp = []
        for temperature in temperatures:
            temp.append((temperature, index))
            index += 1
        
        for temperature in temp:
            if len(stack) == 0:
                stack.append(temperature)
            else:
                if temperature[0] <= stack[-1][0]:
                    stack.append(temperature)
                else:
                    while len(stack) > 0 and temperature[0] > stack[-1][0]:
                        node = stack.pop()
                        result[node[1]] = temperature[1]-node[1]
                    stack.append(temperature)
        return result

print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
