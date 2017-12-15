class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # # Solution 1
        # k = k % len(nums)
        # if k == 0:
        #     temp = []
        # else:
        #     temp = nums[-k:]

        # nums[k:] = nums[:len(nums)-k]
        # nums[:k] = temp

        # # Solution 2
        # k = k % len(nums)
        # i = 0
        # temp = []
        # while i < k:
        #     temp.append(nums.pop())
        #     i += 1
        # i = 0
        # while i < k:
        #     nums.insert(0, temp[i])
        #     i += 1

        # Solution 3
        # stack overflow
        k = k % len(nums)

        def iterate(nums, k):
            if len(nums) > k:
                temp = nums.pop(0)
                iterate(nums, k)
                nums.insert(k, temp)
            else:
                return
        
        iterate(nums, k)

print(Solution().rotate([1,2,3,4,5,6,7], 3))