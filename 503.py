# 给定一个数组, 找到下一个比它大的值, 可以循环. 用栈, 
# 如果压栈的值比栈顶的大, 那么栈顶对应坐标的值修改为压
# 栈的值, 因为可以循环, 所以一开始把数组重复一遍即可

# 优化思路: 压入索引值而不是实际值

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tempNums = []
        i = 0
        for num in nums:
            tempNums.append((num, i))
            i += 1
        tempNums.extend(tempNums)

        stack = []
        greater = {}
        for num in tempNums:
            while len(stack) != 0 and num[0] > stack[-1][0]:
                node = stack.pop()
                greater[node[1]] = num[0]
            stack.append(num)

        result = [-1] * len(nums)
        for i in range(0, len(nums)):
            result[i] = greater.get(i, -1)
        return result

print(Solution().nextGreaterElements([7,3,6,1,4,10,2,100,0]))