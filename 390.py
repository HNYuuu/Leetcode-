class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left2right = True
        remain = n
        step = 1
        head = 1
        while remain > 1:
            if left2right or remain%2 == 1:
                head += step
            remain //= 2
            left2right = not left2right
            step *= 2
        return head
print(Solution().lastRemaining(10))