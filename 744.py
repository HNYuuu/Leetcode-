class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        tempSet = {i for i in letters}
        asciiOf = ord(target)
        i = 1
        while i <= 26:
            if asciiOf + i > 122:
                tempAscii = asciiOf + i - 26
            else:
                tempAscii = asciiOf + i
            if chr(tempAscii) in tempSet:
                return chr(tempAscii)
            i += 1
        
print(Solution().nextGreatestLetter(['a','b'],'c'))
