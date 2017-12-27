# 给一个乱序的字符串, 还原出它原来代表的
# 数字串. 找出数字英语代表的规律即可

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = {}
        for letter in s:
            cache[letter] = cache.get(letter, 0) + 1
        cnt0 = cache.get('z', 0)
        cnt2 = cache.get('w', 0)
        cnt6 = cache.get('x', 0)
        cnt8 = cache.get('g', 0)
        cnt3 = cache.get('h', 0) - cnt8
        cnt4 = cache.get('r', 0) - cnt0 - cnt3
        cnt5 = cache.get('f', 0) - cnt4
        cnt7 = cache.get('v', 0) - cnt5
        cnt9 = cache.get('i', 0) - cnt8 - cnt6 - cnt5
        cnt1 = cache.get('o', 0) - cnt0 - cnt2 - cnt4
        result = '0'*cnt0 + '1'*cnt1 + '2'*cnt2 + '3'*cnt3 + '4'*cnt4 + '5'*cnt5 + '6'*cnt6 + '7'*cnt7 + '8'*cnt8 + '9'*cnt9

        return result

print(Solution().originalDigits('zeroonetwothreefourfivesixseveneightnine'))