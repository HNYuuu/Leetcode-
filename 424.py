class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) < k:
            return len(s)

        store = {}
        for j in range(len(s)):
            store[s[j]] = store.get(s[j], 0) + 1
            if j+1-max(store.values()) > k:
                break
        if j + 1 - max(store.values()) > k:
            window_size = j
        else:
            return len(s)

        i = 1
        store[s[i - 1]] -= 1

        while i + window_size < len(s):
            store[s[i+window_size]] = store.get(s[i+window_size], 0) + 1
            if window_size+1-max(store.values()) <= k:
                window_size += 1
            else:
                store[s[i]] -= 1
                i += 1
        return window_size

print(Solution().characterReplacement("ABCDF", 0))
print(Solution().characterReplacement("ABAB", 2))