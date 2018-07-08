class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        store = []
        for num1 in nums1:
            for num2 in nums2:
                store.append([num1, num2])

        def sift_down(start, end):
            root = start
            while True:
                child = 2*root+1
                if child > end:
                    break
                if child+1 <= end and sum(store[child]) > sum(store[child+1]):
                    child += 1
                if sum(store[root]) > sum(store[child]):
                    store[root], store[child] = store[child], store[root]
                    root = child
                else:
                    break

        for i in range((len(store)-2)//2, -1, -1):
            sift_down(i, len(store)-1)
        for i in range(len(store)-1, len(store)-1-min(len(store), k), -1):
            store[0], store[i] = store[i], store[0]
            sift_down(0, i-1)
        store.reverse()
        return store[:min(len(store), k)]

print(Solution().kSmallestPairs([1,7,11], [2,4,6], 10))