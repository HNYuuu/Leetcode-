class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        result = 0
        i = 0
        while i < len(timeSeries)-1:
            if timeSeries[i+1] - timeSeries[i] >= duration:
                result += duration
            else:
                result += timeSeries[i+1] - timeSeries[i]
            i += 1
        result += duration
        return result