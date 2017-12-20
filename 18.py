# 找出四个相加等于目标值的数, 不允许重复. 一开始的思路是外面两层
# 循环, 里面开始夹逼, 得到一组后判断是否在 result 中, 如果不在
# 加进去; 第一次优化, 不需要判断是否在 result 中, 移动指针令头
# 两个的组合就此失效即可; 第二次优化, 给出了一些极限情况, 在这些
# 情况下直接 break 和 continue 的效率要高很多. 最后从 1700ms
#  优化到 140ms

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for i in range(len(nums)-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3] < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums)-1
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[len(nums)-1] + nums[len(nums)-2] < target:
                    continue
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        
        return results

print(Solution().fourSum([-3,-2,-1,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13]
,0))
