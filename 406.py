# 给一个二维数组，每个元素由两个元素构成。第一个是高度，第二个是一个人可以容忍
# 前面有几个人不低于他。这道题给的思路是贪心，但是实在没有接触过贪心算法，只能
# 用我自己的方法：首先按每个人的容忍度排序，将容忍度低的放到前面，然后再根据容
# 忍度插入别的人，尽量放到后面，就有了我的算法，虽然AC但几乎TLE。
class Solution(object):
    def reconstructQueue(self, peoples):
        """
        :type peoples: List[List[int]]
        :rtype: List[List[int]]
        """
        # AC but nearly TLE
        if peoples == []:
            return []

        kList = [people[1] for people in peoples]
        maxK = max(kList)

        def insertPeople(temp, result):
            for waitPeople in temp:
                count = 0
                i = 0
                while i < len(result) and count <= waitPeople[1]:
                    if result[i][0] >= waitPeople[0]:
                        count += 1
                    i += 1
                if count > waitPeople[1]:
                    result.insert(i-1, waitPeople)
                else:
                    result.append(waitPeople)

        result = []
        temp = []
        for k in range(0, maxK+1):
            for people in peoples:
                if people[1] == k:
                    temp.append(people)
            if len(temp) == 0:
                continue
            for j in temp:
                peoples.remove(j)
            temp = sorted(temp, key=lambda people:people[0])
            if k == 0:
                result.extend(temp)
            else:
                insertPeople(temp, result)
            temp.clear()

        return result

        # Solution 2
        # 第二种思路：首先将最高的人按照k排序，剩下的人按照高度降序排，每一层的人
        # 根据它的k直接插入即可，但是TLE了...可能是方法不太对...
        # if peoples == []:
        #     return []

        # def insertPeople(result, sameHeight):
        #     for people in sameHeight:
        #         result.insert(people[1], people)

        # hList = [people[0] for people in peoples]
        # maxH = max(hList)

        # result = []
        # for i in range(maxH, -1, -1):
        #     sameHeight = [people for people in peoples if people[0] == i]
        #     sameHeight = sorted(sameHeight, key=lambda people:people[1])
        #     for j in sameHeight:
        #         peoples.remove(j)
        #     if i == maxH:
        #         result.extend(sameHeight)
        #     else:
        #         insertPeople(result, sameHeight)
        # return result


print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))