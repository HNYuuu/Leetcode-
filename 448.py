# find all numbers disappeared in an array
# 取负数以标志元素是否只是出现了一次

def find_num(nums):
    result = []
    for i in nums:
        if nums[abs(i)-1] > 0:
            nums[abs(i)-1] = -nums[abs(i)-1]
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i+1)
    return result

if __name__ == '__main__':
    print(find_num([1,1,2,2]))