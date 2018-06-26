class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        final_result = set()

        def backtrack(i, data):
            if len(data) == 4:
                result.append(data.copy())
            else:
                for j in range(i+1, i+4):
                    # 1. unbound error 2. ip num <= 255 3. no pre zeros
                    if j <= len(s) and int(s[i:j]) <= 255 and len(s[i:j]) == len(str(int(s[i:j]))):
                        data.append(s[i:j])
                        backtrack(j, data)
                        data.pop()

        backtrack(0, [])
        for i in result:
            if len(''.join(i)) == len(s):
                final_result.add('.'.join(i))
        return list(final_result)

print(Solution().restoreIpAddresses("010010"))