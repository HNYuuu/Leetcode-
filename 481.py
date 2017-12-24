class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        magic = '122'
        i = 2
        while True:
            if magic[i] == '2' and magic[-1] == '2':
                magic += '11'
            elif magic[i] == '2' and magic[-1] == '1':
                magic += '22'
            elif magic[i] == '1' and magic[-1] == '2':
                magic += '1'
            else:
                magic += '2'
            if len(magic) >= n:
                break
            i += 1
        return magic[:n].count('1')

print(Solution().magicalString(7))