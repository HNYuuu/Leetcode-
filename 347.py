# 给定一个数组，找到出现次数前 k 个元素，要求时间复杂度必须优于
#  O(n logn)。首先构建一个 pair 数组，元素为 (key, times)，
#  因为快排的复杂度最坏为 O(n^2)，所以用堆排序，使用pair 的
#  第二个元素为 key 进行堆排序，调整时只需要调整 k 次输出最大
#  的 k 个就可以了

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tempDict = {}
        for num in nums:
            if num not in tempDict.keys():
                tempDict[num] = 1
            else:
                tempDict[num] += 1
        
        pairs = []
        for key in tempDict:
            pairs.append((key, tempDict[key]))

        result = []
        
        def heapAdjust(pairs, parent, length):
            temp = pairs[parent]
            child = parent * 2 + 1

            while child < length:
                # The right child is bigger than left one
                if child + 1 < length and pairs[child+1][1] > pairs[child][1]:
                    child = child + 1
                
                if temp[1] > pairs[child][1]:
                    break
                pairs[parent] = pairs[child]

                parent = child
                child = parent * 2 + 1
            
            pairs[parent] = temp


        def heapSort(pairs):
            for i in range(len(pairs)//2, -1, -1):
                heapAdjust(pairs, i, len(pairs))
            
            for i in range(len(pairs)-1, len(pairs)-k-1, -1):
                temp = pairs[i]
                pairs[i] = pairs[0]
                pairs[0] = temp

                result.append(pairs[i][0])
                heapAdjust(pairs, 0, i)
        
        heapSort(pairs)
        return result

print(Solution().topKFrequent([1,1,1,2,2,3], 2))
