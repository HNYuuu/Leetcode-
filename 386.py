class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        temp = [str(i) for i in range(1, n+1)]
        temp.sort()
        return [int(i) for i in temp]

print(Solution().lexicalOrder(13))
