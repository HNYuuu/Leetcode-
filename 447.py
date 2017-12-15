class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pair = {}
        result = 0
        for pointA in points:
            for pointB in points:
                if pointA != pointB:
                    distance = (pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2
                    if distance not in pair.keys():
                        pair[distance] = 1
                    else:
                        pair[distance] += 1
            for i in pair.values():
                result += i*(i-1)
            pair.clear()
        return result

print(Solution().numberOfBoomerangs([[0,0],[0,1],[0,2]]))