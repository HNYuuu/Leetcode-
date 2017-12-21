# 找出一个数组中的两个数, 使得这两个数的异或值最大.
#  限制 O(n) 时间. 本来是用字典树做的, 但是在遍历
#  字典树的时候发现每一步得用一次贪心, 没有很好的捋
#  出来递归结构, 而且查了一下发现 trie 也可能 TLE,
#   所以用位操作. 思路就是找到这些数的最左边的那个值, 
#   然后假设该位的最大值是 1, 那么一定有一个这一位是
#   零的数存在在这个数组中, 如果存在, 记录一下最大值
#   的这一位是一, 然后下一位.

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | 1<<i
            tempSet = set()
            for num in nums:
                tempSet.add(num & mask)
            
            temp = maximum | 1<<i
            for prefix in tempSet:
                if prefix ^ temp in tempSet:
                    maximum = temp
                
        return maximum

print(Solution().findMaximumXOR([3,10,5,25,2,8]))