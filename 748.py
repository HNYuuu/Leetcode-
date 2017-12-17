class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        license = list(filter(lambda x:x.isalpha(), licensePlate))
        license = [i.lower() for i in license]
        count = {}
        for i in license:
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1

        def s2d(s):
            temp = {}
            for i in s:
                if i not in temp.keys():
                    temp[i] = 1
                else:
                    temp[i] += 1
            return temp

        words = sorted(words, key=len)
        for word in words:
            right = 0
            temp = s2d(word)
            for i in temp.keys():
                if i in count and temp[i] >= count[i]:
                    right += 1
            if right == len(count.keys()):
                return word

print(Solution().shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))