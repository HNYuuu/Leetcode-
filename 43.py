class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [[0 for _ in range(len(num1)+len(num2))] for _ in range(len(num2))]
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num2)):
            for j in range(len(num1)):
                result[i][-i-j-1] = int(num2[i])*int(num1[j])

        trans = zip(*result)
        trans = trans[::-1]
        result = []
        carry = 0
        for col in trans:
            result.append((sum(col)+carry)%10)
            carry = (sum(col)+carry)//10

        if result.count(0) == len(result):
            return '0'
        else:
            result = map(str, result)
            result = result[::-1]
            i = 0
            while result[i] == '0':
                i += 1
            return ''.join(result[i:])

print(Solution().multiply('2', '3'))
