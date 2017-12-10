class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1, dict2 = {}, {}
        result = []
        for i in nums1:
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in nums2:
            if i not in dict2.keys():
                dict2[i] = 1
            else:
                dict2[i] += 1
        for i in dict1.keys():
            if i in dict2.keys():
                minValue = min(dict1[i], dict2[i])
                temp = [i for x in range(minValue)]
                result.extend(temp)
        return result

print(Solution().intersect([1,2,2,1],[1,2,2,3]))
