# 判断给定的一个矩阵中的连通图的个数。一开始想的
# 简单了，导致本来连通的图计算上令其分开了。然后
# 发现这道题是要用并查集的，于是构造 find 和 
# union 函数，parent 数组构造完成后对每一个寻
# 找根节点，将所有的根节点值扔到一个 set 中，返
# 回 set 的长度

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        parent = [i for i in range(0, N)]
        rank = [0] * N

        def findParent(x):
            if parent[x] == x:
                return parent[x]
            parent[x] = findParent(parent[x])
            return parent[x]

        def union(x, y):
            px = findParent(x)
            py = findParent(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                parent[py] = px
            else:
                if rank[py] == rank[px]:
                    rank[py] += 1
                parent[px] = py
        
        for i in range(0, N):
            for j in range(i+1, N):
                if M[i][j] == 1:
                    union(i, j)

        parents = set()
        for i in range(0, N):
            parents.add(findParent(i))
        return len(parents)
 

print(Solution().findCircleNum([[1,1,0],
 [1,1,0],
 [0,0,1]]))