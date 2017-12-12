class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowelsIn = list(filter(lambda x: x in vowels, s))
        vowelsIn.reverse()
        result = []
        j = 0
        for i in s:
            if i not in vowels:
                result.append(i)
            else:
                result.append(vowelsIn[j])
                j += 1
        return "".join(result)

print(Solution().reverseVowels('aA'))