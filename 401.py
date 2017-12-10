class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8:
            return []
        hourLight, minLight = 0, 0
        hArray, mArray = [], []
        result = []
        while hourLight < min(3, num)+1:
            minLight = num - hourLight
            if minLight > 5:
                hourLight += 1
                continue
            hArray = self.validBits(hourLight, 12)
            mArray = self.validBits(minLight, 60)
            for i in hArray:
                for j in mArray:
                    result.append(i + ':' + j)
            hourLight += 1        
        
        return result

    def validBits(self, num, limit):
        temp = []
        for i in range(limit):
            if limit == 60:
                if bin(i)[2:].count('1') == num:
                    if i < 10:
                        temp.append('0'+str(i))
                    else:
                        temp.append(str(i))
            else:
                if bin(i)[2:].count('1') == num:
                    temp.append(str(i))
        return temp

print(Solution().readBinaryWatch(7))