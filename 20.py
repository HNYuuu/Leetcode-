class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if s.count('(')+s.count('[')+s.count('{') != s.count(')')+s.count(']')+s.count('}'):
            return False
        for i in s:
            temp = ''
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) != 0:
                    temp = stack.pop()
                else:
                    return False
                if temp+i != '()' and temp+i != '[]' and temp+i != '{'+'}':
                    return False
        return True

print(Solution().isValid('){'))