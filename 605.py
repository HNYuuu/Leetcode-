class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0,0)
        flowerbed.insert(0,1)
        flowerbed.append(0)
        flowerbed.append(1)
        i = 0
        flower = []
        result = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                flower.append(i)
            i += 1
        i = 0
        while i < len(flower)-1:
            space = flower[i+1]-flower[i]-1
            if space%2 == 1:
                result += space//2
            else:
                result += space//2-1
            i += 1
        return True if result >= n else False

print(Solution().canPlaceFlowers([0,1,1]
,1))