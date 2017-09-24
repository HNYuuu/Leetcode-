# next closest time

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour = time[0:2]
        minute = time[-2:]
        all_number = set(hour+minute)
        op_h = int(hour)
        op_m = int(minute)
        while True:
            if op_m < 59:
                op_m += 1
            else:
                op_m = 0
                if op_h < 23:
                    op_h += 1
                else:
                    op_h = 0
            temp_h = str(op_h).zfill(2)
            temp_m = str(op_m).zfill(2)
            temp = temp_h + temp_m
            flag = 0
            for i in temp:
                if i not in all_number:
                    flag = 1
                    break
            if flag == 1:
                continue
            else:
                return temp_h + ':' + temp_m

s = Solution()
print(s.nextClosestTime("23:59"))