class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for i in nums:
            if max1 == float('-inf'):
                max1 = i
            elif max2 == float('-inf'):
                if max1 > i:
                    max2 = i
                elif max1 < i:
                    max2 = max1
                    max1 = i
                else:
                    continue
            else:
                if i > max1:
                    max3 = max2
                    max2 = max1
                    max1 = i
                elif i < max1 and i > max2:
                    max3 = max2
                    max2 = i
                elif i < max2 and i > max3:
                    max3 = i
                else:
                    continue
        return max1 if max3 == float('-inf') else max3

print(Solution().thirdMax([5,2,4,1,3,6,0]))