class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []

        my_set = set()
        result_set = set()

        for i in range(10, len(s)+1):
            if s[i-10:i] not in my_set:
                my_set.add(s[i-10:i])
            else:
                result_set.add(s[i-10:i])

        return list(result_set)


print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAA"))
