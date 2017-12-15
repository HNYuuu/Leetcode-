class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binstr = bin(n)[2:].zfill(32)
        binlist = [i for i in binstr]
        binlist.reverse()
        reverseStr = "".join(binlist)
        return int(reverseStr, 2)

print(Solution().reverseBits(43261596))