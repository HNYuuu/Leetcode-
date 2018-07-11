class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        if len(start) != len(end):
            return -1

        needed = set()
        visited = set()

        def strHamming(s, t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
            return count

        needed.add(start)
        result = 0
        while len(needed) > 0:
            length = len(needed)
            for _ in range(length):
                temp_s = needed.pop()
                if temp_s == end:
                    return result
                visited.add(temp_s)
                for bk in bank:
                    if strHamming(temp_s, bk) == 1 and bk not in visited:
                        needed.add(bk)
            result += 1

        return -1

print(Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(Solution().minMutation("AACCGGTT", "AACCGCTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(Solution().minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))