import math

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def adjustHeap(i):
            lchild = heap[2*i+1] if 2*i+1 < len(heap) else float('inf')
            rchild = heap[2*i+2] if 2*i+2 < len(heap) else float('inf')
            if lchild <= rchild and lchild < heap[i]:
                heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
                adjustHeap(2*i+1)
            if rchild < lchild and rchild < heap[i]:
                heap[i], heap[2*i+2] = heap[2*i+2], heap[i]
                adjustHeap(2*i+2)
            
        heap = []
        for row in matrix:
            heap.extend(row)
        
        length = len(heap)
        for i in range(math.ceil((length-2)//2), -1, -1):
            adjustHeap(i)

        for i in range(0, k):
            temp = heap[0]
            heap[0] = heap.pop()
            adjustHeap(0)
        return temp

print(Solution().kthSmallest([
   [13,  5,  9],
   [105, 1, 13],
   [12, 3, 15]
], 8))