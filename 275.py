class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0

        l, r = 0, len(citations)-1
        length = len(citations)

        while r-l > 1:
            m = l+(r-l)//2
            if length-m <= citations[m]:
                r = m
            else:
                l = m
        if length-l <= citations[l]:
            return length-l
        elif length-r <= citations[r]:
            return length-r
        else:
            return 0

print(Solution().hIndex([100]))