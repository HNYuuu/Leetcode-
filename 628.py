# maximum product of three numbers

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        neg = filter(self.negative, nums)
        pos = filter(self.positive, nums)
        zero = filter(self.zero_fil, nums)
        if len(neg) == 0:
            return self.mutiply_3(self.max_three(pos))
        elif len(pos) == 0:
            if len(zero) != 0:
                return 0
            else:
                return self.mutiply_3(self.max_three(neg))
        else:
            if len(pos) > 2:
                if len(neg) == 1:
                    return self.mutiply_3(self.max_three(pos))
                else:
                    temp_neg = self.max_two(neg)
                    temp_pro = temp_neg[0]*temp_neg[1]
                    return max(temp_pro*max(pos), self.mutiply_3(self.max_three(pos)))
            else:
                temp_neg = self.max_two(neg)
                temp_pro = temp_neg[0]*temp_neg[1]
                return temp_pro*max(pos)

    def positive(self, x):
        return x>=0

    def negative(self, x):
        return x<0

    def zero_fil(self, x):
        return x==0

    def max_three(self, nums):
        top1 = max(nums)
        nums.remove(top1)
        top2 = max(nums)
        nums.remove(top2)
        top3 = max(nums)
        nums.remove(top3)
        return top1, top2, top3

    def max_two(self, nums):
        nums = list(map(abs, nums))
        top1 = max(nums)
        nums.remove(top1)
        top2 = max(nums)
        return top1, top2

    def mutiply_3(self, nums):
        return nums[0]*nums[1]*nums[2]

s = Solution()
print(s.maximumProduct([0,0,0,4]))