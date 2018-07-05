class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        length = len(citations)

        for i in range(length):
            if length-i <= citations[i]:
                return length-i
        return 0

print(Solution().hIndex([]))