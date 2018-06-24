class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = 0
        score = [0 for _ in range(30)]

        def count(layer):
            if score[layer+1] == 0:
                score[layer] += 1
            else:
                score[layer] += 2*(score[layer+1])
                # erase the next layer's score
                score[layer+1] = 0

        for i in S:
            if i == '(':
                stack += 1
            else:
                count(stack)
                stack -= 1
        return score[1]

print(Solution().scoreOfParentheses("(())()"))