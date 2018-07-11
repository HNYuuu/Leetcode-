# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        store = sorted(intervals, key=lambda x: x.start)
        index = {}
        for i in range(len(intervals)):
            if intervals[i] not in index.keys():
                index[intervals[i]] = i

        result = []

        def binarySearch(num):
            l = 0
            r = len(store)-1
            while r-l > 1:
                m = l + (r-l)//2
                if store[m].start > num:
                    r = m
                elif store[m].start < num:
                    l = m
                else:
                    return m
            if store[l].start >= num:
                return l
            elif store[r].start >= num:
                return r
            return -1

        for interval in intervals:
            need = interval.end
            temp = binarySearch(need)
            if temp == -1:
                result.append(-1)
            else:
                result.append(index[store[temp]])

        return result

a = Interval(3,4)
b = Interval(2,3)
c = Interval(1,2)

print(Solution().findRightInterval([a,b,c]))