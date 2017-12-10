class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        temp = []
        for i in s:
            temp.append(i)
        i = 0
        while i < len(temp):
            if i+k < len(temp):
                temp[i:i+k] = temp[i:i+k][::-1]
            else:
                temp[i:] = temp[i:][::-1]
                break
            i += 2*k
        return "".join(temp)

print(Solution().reverseStr('abcdefg', 2))