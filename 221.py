class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])

        flag = True
        now_max = 0
        now_k = 0
        for i in range(len(matrix)):
            j = 0
            while j < len(matrix[0]):
                for k in range(1,min(len(matrix)-i, len(matrix[0])-j)+1):
                    if k <= now_k:
                        continue
                    if sum(matrix[i][j:j+k]) == k:
                        for t in range(k):
                            if sum(matrix[i+t][j:j+k]) != k:
                                flag = False
                                break
                        if not flag:
                            flag = True
                            break
                        else:
                            if k*k > now_max:
                                now_max = k*k
                                now_k = k
                    else:
                        break
                # if sum(matrix[i][j:j+k]) == k:
                #     j += 1
                # else:
                #     j += k
                j += 1
        return now_max

print(Solution().maximalSquare([["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]))