class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [] or strs[0] == '':
            return ''
        index = 0
        terminate = False
        while index < len(strs[0]):
            prefix = strs[0][0:index+1]
            for i in strs:
                if len(i) > index and i[0:index+1]==prefix:
                    continue
                else:
                    terminate = True
                if terminate:
                    break
            if terminate:
                return prefix[:-1]
            else:
                index += 1
        return prefix

print(Solution().longestCommonPrefix(['ab','ab','abc','d']))
