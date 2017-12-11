class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num += 2**32
        remainders = []
        while num//16 != 0:
            remainder = num%16
            if remainder < 10:
                remainders.append(str(remainder))
            else:
                remainders.append(chr(remainder+87))
            num = num//16
        if num < 10:
            remainders.append(str(num))
        else:
            remainders.append(chr(num+87))
        return "".join(remainders[::-1])

print(Solution().toHex(-1))