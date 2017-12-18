# 给一些字符串，然后再给一个，判断这个字符串是不是距离一开始中的
# 任意一个编辑距离为一。构造字典，键为给定的单词，值为它可能改变
# 的样子，用 '_' 填充空位，将要查找的单词修改成可能的样子，检查
# 在不在字典的值中，并且键和给定的单词不相等

class MagicDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.magic = {}

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type words: List[str]
        :rtype: void
        """
        value = []
        for word in words:
            i = 0
            while i < len(word):
                value.append(word[:i]+'_'+word[i+1:])
                i += 1
            self.magic[word] = value.copy()
            value.clear()

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        i = 0
        temp = []
        while i < len(word):
            temp.append(word[:i]+'_'+word[i+1:])
            i += 1
        for uglyword in temp:
            for key in self.magic.keys():
                if word != key and uglyword in self.magic[key]:
                    return True
        return False
            


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(['a', 'b', 'ab'])
param_2 = obj.search('ba')
print(param_2)