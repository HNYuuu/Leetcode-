class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        appear = []
        count = {}
        for i in nums:
            if i not in count.keys():
                count[i] = 1
                appear.append(i)
            else:
                count[i] += 1
        appear.sort()
        i = 0
        maximum = 0
        while i < len(appear)-1:
            if abs(appear[i]-appear[i+1]) == 1:
                temp = count[appear[i]]+count[appear[i+1]]
                if temp > maximum:
                    maximum = temp
            i += 1
        return maximum

print(Solution().findLHS([2,3,2,4,7,1,3,2]))
