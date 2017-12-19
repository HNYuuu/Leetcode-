# 一个房间有 n 个灯泡，4个开关，每个开关有一
# 种操作方式，一共进行 m 次操作，问可能的结果。
# 其实用列表法可以找到规律，然后方法之间可以组
# 合等效，因此只需要分情况，O(1)即可

class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2 and m == 1:
            return 3
        if n == 2:
            return 4
        if m == 1:
            return 4
        if m == 2:
            return 7
        return 8