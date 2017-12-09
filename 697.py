class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numberAppear = {}
        minLength = 60000
        for i in nums:
            if i not in numberAppear.keys():
                numberAppear[i] = nums.count(i)
        maximum = max(numberAppear.values())
        if maximum == 1:
            return 1
        else:
            for i in numberAppear.keys():
                if numberAppear[i] != maximum:
                    continue
                else:
                    tempA = nums.index(i)
                    nums.reverse()
                    tempB = len(nums)-nums.index(i)
                    result = abs(tempA-tempB)
                    if result < minLength:
                        minLength = result
        return minLength


print(Solution().findShortestSubArray([1,1,1,2,2,3,4,5,6,2,3,4,3]))
