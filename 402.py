class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # brute force, TLE

        # another solution
        # maintain a increasing stack
        if len(num) == k:
            return '0'

        stack = []
        for n in num:
            while len(stack) > 0 and k > 0 and n<stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0:
            stack.pop()
            k -= 1
        return str(int(''.join(stack)))


print(Solution().removeKdigits("112", 1))
print(Solution().removeKdigits("1432219",3))
print(Solution().removeKdigits("1",1))
