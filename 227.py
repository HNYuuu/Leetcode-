class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}

        stack = []
        output = []

        op = 0
        while op < len(s):
            if s[op] == ' ':
                op += 1
                continue
            elif s[op].isdigit():
                temp = s[op]
                while op + 1 < len(s) and s[op+1].isdigit():
                    temp += s[op+1]
                    op += 1
                output.append(int(temp))
                op += 1
                continue
            else:
                this_priority = priority[s[op]]
                while len(stack) > 0:
                    if priority[stack[-1]] >= this_priority:
                        output.append(stack.pop())
                    else:
                        break
                stack.append(s[op])
                op += 1
        while len(stack) > 0:
            output.append(stack.pop())

        # output now is the RPN
        stack = []
        for op in output:
            if isinstance(op, int):
                stack.append(op)
            elif op == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif op == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif op == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif op == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)

        return stack[0]


print(Solution().calculate('2+3*3/4+5*6-34'))
