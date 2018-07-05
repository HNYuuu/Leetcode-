class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        first = 0
        first_element = nums[first]
        last = 1
        result = []
        while last < len(nums):
            if nums[last] == nums[last-1]+1:
                last += 1
            else:
                if last-1 == first:
                    result.append(str(first_element))
                else:
                    result.append(str(first_element) + '->' + str(nums[last-1]))
                first = last
                first_element = nums[first]
                last = first + 1
        if last - 1 == first:
            result.append(str(first_element))
        else:
            result.append(str(first_element) + '->' + str(nums[last - 1]))
        return result

print(Solution().summaryRanges([0]))