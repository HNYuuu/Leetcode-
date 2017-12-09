class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        init = False if s[0] == '0' else True
        now = False
        result = 0
        serial = []
        for i in s:
            now = False if i == '0' else True
            if now == init:
                result += 1
            else:
                serial.append(result)
                init = now
                result = 1
        serial.append(result)
        # return serial
        result = 0
        for i in range(len(serial)-1):
            j = i+1
            result += min(serial[i], serial[j])
        return result



print(Solution().countBinarySubstrings('001110011'))