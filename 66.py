class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        i = length - 1
        carry = False
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                carry = False
                break
            else:
                digits[i] = 0
                carry = True
            i -= 1
        if carry:
            digits.insert(0,1)
        return digits

print(Solution().plusOne([9,9,9,9,9,9,8]))