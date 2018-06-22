# -*- coding: utf-8 -*-

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        difs = []
        for standard in range(len(nums)-2):
            # 第一处优化
            if standard > 0 and nums[standard] == nums[standard-1]:
                difs.append(difs[standard-1])
                continue
            t_i = target - nums[standard]
            l, r = standard+1, len(nums)-1
            difs.append(nums[l]+nums[r]-t_i)
            while r-l > 1:
                if nums[l] + nums[r] < t_i:
                    l += 1
                    if nums[l] == nums[l-1]:
                        continue
                    if abs(difs[standard]) > abs(nums[l]+nums[r]-t_i):
                        difs[standard] = nums[l]+nums[r]-t_i
                    # else:
                    #     break
                elif nums[l] + nums[r] > t_i:
                    r -= 1
                    if nums[r] == nums[r+1]:
                        continue
                    if abs(difs[standard]) > abs(nums[l]+nums[r]-t_i):
                        difs[standard] = nums[l]+nums[r]-t_i
                    # else:
                    #     break
                else:
                    difs[standard] = 0
                    break
        min_index = difs.index(min(difs, key=abs))
        return difs[min_index] + target

print(Solution().threeSumClosest([6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10],-52))