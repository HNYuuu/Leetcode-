class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        result = {'A': 0, 'B': 0}

        secret_dict = {}
        for c in secret:
            secret_dict[c] = 1 if c not in secret_dict.keys() else 1+secret_dict[c]

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                result['A'] += 1
                secret_dict[secret[i]] -= 1

        for i in range(len(secret)):
            if guess[i] in secret_dict.keys() and secret_dict[guess[i]] != 0 and guess[i] != secret[i]:
                result['B'] += 1
                secret_dict[guess[i]] -= 1

        return str(result['A']) + 'A' + str(result['B']) + 'B'

print(Solution().getHint('1122', '1222'))