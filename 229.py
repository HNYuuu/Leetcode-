class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Moore voting
        store1, store2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if store1 is None and store2 is None:
                store1 = num
                count1 += 1
            elif store1 is None and num != store2:
                store1 = num
                count1 += 1
            elif store2 is None and num != store1:
                store2 = num
                count2 += 1
            elif num == store1:
                count1 += 1
            elif num == store2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                if count1 == 0:
                    store1 = None
                if count2 == 0:
                    store2 = None
        result = []
        if store1 is not None and nums.count(store1) > len(nums)//3:
            result.append(store1)
        if store2 is not None and nums.count(store2) > len(nums)//3:
            result.append(store2)
        return result

print(Solution().majorityElement([1,2,1,1,1,3,3,4,3,3,3,4,4,4]))