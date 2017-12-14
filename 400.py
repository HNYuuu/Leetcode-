import math

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        def total(layer):
            return ((9*layer-1)*(10**layer)+1)//9
        layersTotal = []
        layer = 1
        layersTotal.append(total(1))
        while n > layersTotal[-1]:
            layer += 1
            layersTotal.append(total(layer))

        whichDigit = (n-(layersTotal[layer-2]))%(layer)

        numberOffset = math.ceil((n-layersTotal[layer-2])/layer)
        number = 10**(layer-1)+(numberOffset-1)

        numberList = [i for i in str(number)]

        return int(numberList[whichDigit-1])

        # return layer, layersTotal, whichDigit, numberOffset, number, numberList

print(Solution().findNthDigit(10000))

