# 实现一个复数的乘法。找到加号的位置，然后提取出来四个操作
# 数，代入公式即可。

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        addPositionA = a.index('+')
        addPositionB = b.index('+')
        aa = int(a[:addPositionA])
        ab = int(a[addPositionA+1:-1])
        ba = int(b[:addPositionB])
        bb = int(b[addPositionB+1:-1])

        a = str(aa*ba-ab*bb)
        b = str(ab*ba+aa*bb)

        return a+'+'+b+'i'

print(Solution().complexNumberMultiply('1+-1i', '1+-1i'))