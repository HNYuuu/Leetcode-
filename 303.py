class NumArray:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cache = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.cache[i:j+1])
        


# Your NumArray object will be instantiated and called as such:
obj = NumArray([0,1,2,3,4,5])
param_1 = obj.sumRange(0,4)
print(param_1)