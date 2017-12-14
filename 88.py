class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, count = 0, 0, 0
        while i < m+count and j < n:
            if nums1[i] > nums2[j]:
                nums1[i+1:m+count+1] = nums1[i:m+count]
                nums1[i] = nums2[j]
                j += 1
                count += 1
            i += 1
        if i == m+count:
            nums1[i:] = nums2[j:n+1]
        print(nums1)

Solution().merge([4,0,0,0,0,0]
,1
,[1,2,3,5,6]
,5)
