from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        max_len = len(max(nums, key=len))

        # 824, 8247 is wrong for this strategy
        # nums.sort(key=lambda num: num + (max_len - len(num)) * num[-1], reverse=True)
        def my_cmp(a,b):
            if a+b < b+a:
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(my_cmp), reverse=True)

        while len(nums)>1:
            if int(nums[0]) == 0:
                del nums[0]
            else:
                break

        return ''.join(nums)


print(Solution().largestNumber([0,0,0]))
