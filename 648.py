# 将一个句子中的单词改为前缀形式如果有的话. 思路一: 构建一个
#  prefix 的 set, 然后遍历每个单词的所有前缀, 如果前缀在 
#  set 中的话替换, 没有的话就用原单词. 思路二: 构建字典树, 
#  使用 dict 来构建, 比之前的快很多

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # Solution 1 hash table and map func
        # prefixes = set(dict)

        # def match(word):
        #     for i in range(1, len(word)):
        #         if word[:i] in prefixes:
        #             return word[:i]
        #     return word

        # return ' '.join(map(match, sentence.split()))

        # Solution 2 trie FASTER
        def buildTrie(dictionary):
            trie = {}
            for word in dictionary:
                cur = trie
                for letter in word:
                    if letter not in cur:
                        cur[letter] = {}
                    cur = cur[letter]
                cur[''] = True
            return trie

        def findInTrie(word, trie):
            cur = trie
            path = []
            for letter in word:
                if len(path) > 0 and '' in cur:
                    return ''.join(path)
                if letter not in cur.keys():
                    return ''
                cur = cur[letter]
                path.append(letter)
            return ''


        trie = buildTrie(dict)
        result = []
        for word in sentence.split():
            newWord = findInTrie(word, trie)
            if newWord == '':
                newWord = word
            result.append(newWord)
        return ' '.join(result)

print(Solution().replaceWords(["cat", "bat", "rat"]
,"the cattle was rattled by the battery"))