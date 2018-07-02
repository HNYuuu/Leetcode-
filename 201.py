class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return n

        bin_m, bin_n = bin(m)[2:], bin(n)[2:]
        max_len = max(len(bin_m), len(bin_n))
        if len(bin_m)<len(bin_n):
            bin_m = bin_m.zfill(max_len)
        else:
            bin_n = bin_n.zfill(max_len)
        bin_n = bin_n[::-1]
        bin_m = bin_m[::-1]

        mask = ['1' for _ in range(32)]
        for x in range(max_len):
            if n-m >= 2**x:
                mask[x] = '0'
            else:
                if bin_n[x] != bin_m[x]:
                    mask[x] = '0'

        mask.reverse()
        mask_int = int(''.join(mask), 2)
        return m&mask_int

print(Solution().rangeBitwiseAnd(5,7))