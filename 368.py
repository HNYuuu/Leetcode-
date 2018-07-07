class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 1:
            return []

        store = [1 for _ in range(len(nums))]
        # record the parent's position
        store_j = [-1 for _ in range(len(nums))]

        nums.sort()

        def dp(i):
            if i == 0:
                return 1
            elif store[i] != 1:
                # print('hit')
                return store[i]
            tmp = []
            tmp_j = []
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    tmp.append(dp(j) + 1)
                    tmp_j.append(j)
            tmp.append(store[i])
            tmp_j.append(i)
            store[i] = max(tmp)
            store_j[i] = tmp_j[tmp.index(max(tmp))]

            return store[i]

        for i in range(len(nums)):
            dp(i)

        result = []
        j = store.index(max(store))
        result.append(nums[j])
        while store_j[j] != -1 and j != store_j[j]:
            j = store_j[j]
            result.append(nums[j])

        return result


print(Solution().largestDivisibleSubset([3,4,16,8]))
