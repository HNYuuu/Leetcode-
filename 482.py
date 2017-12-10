class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        array = [i for i in S]
        array = list(filter(lambda x: x != '-', array))
        remainder = len(array) % K
        firstPart = "".join(array[0:remainder])
        i = remainder
        while i < len(array):
            firstPart = firstPart + '-' + "".join(array[i:i+K])
            i += K
        return firstPart.upper()[1:] if remainder == 0 else firstPart.upper()

print(Solution().licenseKeyFormatting('kj-2jk-bis4-j', 4))