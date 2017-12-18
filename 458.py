import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0
        status = math.floor(minutesToTest/minutesToDie)+1
        i = 1
        while status**i < buckets:
            i += 1
        return i

print(Solution().poorPigs(3126, 15, 60))