class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            elif i < len(bits)-1:
                i += 1
            else:
                return True
        return False