# 洗牌算法

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prototype = nums.copy()
        self.cache = nums.copy()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.prototype

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        result = []
        for i in range(len(self.cache), 0, -1):
            shuffle = random.randrange(0, i)
            result.append(self.cache[shuffle])
            self.cache.remove(self.cache[shuffle])
        self.cache = self.prototype.copy()
        return result


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,4,5,6,7,8,9])
param_1 = obj.reset()
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
