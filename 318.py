# 给定一个字符串数组, 找到两个不包含相同字母的字符串, 
# 计算这样的字符串对的长度乘积的最大值. 用bit串代表a-z 
# 26个字母, 然后进行一个n^2的与运算, 如果结果是零, 
# 计算两个对应词的长度, 取最大值

class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bits = [0] * len(words)

        i = 0
        for word in words:
            for letter in word:
                bits[i] |= 1<<(122-ord(letter))
            i += 1
        
        maximum = 0
        for i in range(len(bits)-1):
            for j in range(i+1, len(bits)):
                if bits[i] & bits[j] == 0:
                    maximum = max(maximum, len(words[i])*len(words[j]))
        return maximum

print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))