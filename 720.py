class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        tempset = set()
        for word in words:
            if len(word) == 1:
                tempset.add(word)
        words.sort()
        # return tempset, words
        for word in words:
            if word[0:-1] in tempset:
                tempset.add(word)
        maximum = max(len(i) for i in tempset)
        array = []
        for word in tempset:
            if len(word) == maximum:
                array.append(word)
        array.sort()
        return array[0]

print(Solution().longestWord(["k","lg","it","oidd","oid","oiddm","kfk","y","mw","kf","l","o","mwaqz","oi","ych","m","mwa"]))