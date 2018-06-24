class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        cur, next, tmp = 0, 1, 2
        while cur < len(nums)-2:
            if nums[cur] != nums[next]:
                cur += 1
                next += 1
                tmp += 1
            else:
                if nums[tmp] == nums[next]:
                    del nums[tmp]
                else:
                    cur, next = tmp, tmp+1
                    tmp = next+1

        return len(nums)

print(Solution().removeDuplicates([1,2,2,3]))