class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        f0 = 0
        for i in range(len(A)):
            f0 += i*A[i]

        my_max = f0
        last_result = f0
        my_sum = sum(A)
        for i in range(len(A)-1, 0, -1):
            temp = last_result+my_sum-len(A)*A[i]
            if temp > my_max:
                my_max = temp
            last_result = temp

        return my_max

print(Solution().maxRotateFunction([4,2]))