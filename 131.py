class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        store = [[False for _ in range(len(s)+1)] for _ in range(len(s))]
        for i in range(len(s)):
            store[i][i+1] = True
        for i in range(len(s)-1):
            j = i+2
            if s[i] == s[j-1]:
                store[i][j] = True

        # recursive along the dialog direction
        for k in range(len(s)-2, 0, -1):
            for i in range(k):
                j = len(s)-k+i+1
                store[i][j] = store[i+1][j-1] and (s[i] == s[j-1])

        result = []
        def backtrack(i, data):
            if i == len(s):
                result.append(data.copy())
            else:
                for j in range(i+1, len(s)+1):
                    if store[i][j] == True:
                        data.append(s[i:j])
                        backtrack(j, data)
                        data.pop()

        backtrack(0, [])
        return result

print(Solution().partition(''))