import math


class Solution:
    def isAdditiveNumber(self, s):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, math.ceil(len(s) / 2)):
            for j in range(i + 1, len(s)):
                if i > 1 and s[0] == '0':
                    break
                else:
                    first_num = int(s[:i])
                if j-i > 1 and s[i] == '0':
                    break
                else:
                    second_num = int(s[i:j])

                while True:
                    third_num = str(first_num+second_num)
                    length = len(third_num)
                    if j+length < len(s) and s[j:j+length] == third_num:
                        first_num = second_num
                        second_num = int(third_num)
                        j = j + length
                    elif j+length == len(s) and s[j:j+length] == third_num:
                        return True
                    else:
                        break
        return False

print(Solution().isAdditiveNumber("101"))