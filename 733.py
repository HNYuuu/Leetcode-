class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        queue = []
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        queue.append((sr,sc))
        while queue:
            temp = queue.pop(0)
            i = temp[0]
            j = temp[1]
            image[i][j] = newColor
            if i>0 and (i-1,j) not in queue and image[i-1][j] == oldColor:
                queue.append((i-1,j))
            if i<len(image)-1 and (i+1,j) not in queue and image[i+1][j] == oldColor:
                queue.append((i+1,j))
            if j>0 and (i,j-1) not in queue and image[i][j-1] == oldColor:
                queue.append((i,j-1))
            if j<len(image[0])-1 and (i,j+1) not in queue and image[i][j+1] == oldColor:
                queue.append((i,j+1))
        return image

print(Solution().floodFill([[0,0,0],[0,1,1]], 1, 1, 1))