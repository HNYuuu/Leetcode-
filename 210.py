class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degree = [0 for _ in range(numCourses)]
        result = []

        # pairs = set([tuple(x) for x in prerequisites])
        pairs = prerequisites
        for pair in pairs:
            degree[pair[1]] += 1

        my_queue = []
        for i in range(len(degree)):
            if degree[i] == 0:
                my_queue.append(i)

        while len(my_queue)>0:
            post = my_queue.pop()
            result.append(post)
            j = 0
            while j<len(pairs):
                if pairs[j][0] == post:
                    degree[pairs[j][1]] -= 1
                    if degree[pairs[j][1]] == 0:
                        my_queue.append(pairs[j][1])
                    del pairs[j]
                    continue
                j += 1

        if sum(degree):
            return []
        else:
            return result[::-1]

print(Solution().canFinish(3, [[2,1],[2,0]]))