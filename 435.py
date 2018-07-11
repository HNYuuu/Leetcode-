# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        # greedy
        intervals.sort(key=lambda x:(x.end, x.start))

        count = 0
        i = 0
        while True:
            next = intervals[i].end
            count += 1
            find_it = False
            for j in range(i, len(intervals)):
                if intervals[j].start >= next:
                    find_it = True
                    break
            if find_it:
                i = j
            else:
                break

        return len(intervals)-count

a = Interval(0,1)
b = Interval(1,2)
c = Interval(3,4)
d = Interval(1,3)
print(Solution().eraseOverlapIntervals([a,b,c,d]))
# print(Solution().eraseOverlapIntervals([a,b,c]))