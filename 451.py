class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = {}
        for i in s:
            if i not in temp.keys():
                temp[i] = 1
            else:
                temp[i] += 1
        
        temp2 = []
        for key in temp.keys():
            temp2.append((key, temp[key]))
        
        temp2 = sorted(temp2, key=lambda x: x[1], reverse=True)
        result = ''
        for i in temp2:
            result += i[0]*i[1]
        return result

print(Solution().frequencySort('apple'))
