class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0, len(height)-1
        base = (r-l)*min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            rec = (r-l)*min(height[l], height[r])
            if rec > base:
                base = rec

        return base

print(Solution().maxArea([3, 1]))