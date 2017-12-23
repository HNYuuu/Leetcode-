# 给定一些合法的时间点, 找出最小时间差, 三种方法. 第一种最为复杂, 
# 将没有排序的输入进来, 先计算相邻点的顺时针和逆时针方向距离, 再
# 通过相加余1440可以得到任意两个时间点的顺逆时针距离, 但是最后一
# 个测试用例有 20000 个时间点, TLE; 第二种发现可以先用小时排序, 
# 再用分钟排序, 这样可以得到一个递增的时间点, 只需要相邻的时间差
# 就可以, 只超过了 3%; 第三种直接对每一个时间点计算它现在的分钟
# 数, 然后快排, 比较相邻差以及最后一个和开头的差得到最小值, 超
# 过 100%

from operator import itemgetter

class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # def twoDiffMinutes(time1, time2):
        #     time1split = time1.split(':')
        #     time2split = time2.split(':')
        #     t1h = time1split[0]
        #     t1m = time1split[1]
        #     t2h = time2split[0]
        #     t2m = time2split[1]

        #     def calcDiff(h1, h2, m1, m2):
        #         if int(m1)-int(m2) >= 0:
        #             carry = False
        #             mdiff = int(m1)-int(m2)
        #         else:
        #             carry = True
        #             mdiff = int(m1)-int(m2)+60

        #         if carry:
        #             h1 = str(int(h1)-1)
        #         if int(h1) < int(h2):
        #             h1 = str(int(h1)+24)
        #         hdiff = int(h1)-int(h2)

        #         return (hdiff, mdiff)

        #     (h1diff, m1diff) = calcDiff(t1h, t2h, t1m, t2m)
        #     (h2diff, m2diff) = calcDiff(t2h, t1h, t2m, t1m)

        #     return min(h1diff*60+m1diff, h2diff*60+m2diff)

        # def combine(time1, time2):
        #     counter1 = time1[0]
        #     clock1 = time1[1]
        #     counter2 = time2[0]
        #     clock2 = time2[1]
        #     return ((counter1+counter2)%1440, (clock1+clock2)%1440)

        # Solution1 TLE on the last excution
        # store = {}
        # for i in range(0, len(timePoints)-1):
        #     j = i+1
        #     store[(i, j)] = twoDiffMinutes(timePoints[i], timePoints[j])
        #     for j in range(0, i):
        #         store[(j, i+1)] = combine(store[(j, i)], store[(i, i+1)])

        # resultMinutes = []
        # for value in store.values():
        #     resultMinutes.append(value[0])
        #     resultMinutes.append(value[1])

        # if 1440 in resultMinutes:
        #     return 0
        # else:
        #     return min(resultMinutes)

        # Solution2 AC but a little bit slow
        # minimum = float('inf')
        # timePoints = sorted(timePoints, key=itemgetter(slice(0,2), slice(3,None)))
        # for i in range(0, len(timePoints)-1):
        #     minimum = min(minimum, twoDiffMinutes(timePoints[i], timePoints[i+1]))
        # minimum = min(minimum, twoDiffMinutes(timePoints[len(timePoints)-1], timePoints[0]))

        # return minimum

        # Solution3 AC beat 100%!!!
        minutes = []
        for time in timePoints:
            minutes.append(int(time[0:2])*60+int(time[3:]))
        minutes.sort()
        minimum = float('inf')
        for i in range(0, len(minutes)-1):
            minimum = min(minimum, minutes[i+1]-minutes[i])
        minimum = min(minimum, minutes[0]-minutes[-1]+1440)
        return minimum


print(Solution().findMinDifference())