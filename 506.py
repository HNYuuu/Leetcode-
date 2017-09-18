# relative ranks

def solution(nums):
    result = [-1 for i in range(len(nums))]
    count = 1
    while count <= len(nums):
        maximum = max(nums)
        temp_index = nums.index(maximum)
        result[temp_index] = str(count)
        count += 1
        nums[temp_index] = -1
    if '1' in result:
        result[result.index('1')] = 'Gold Medal'
    if '2' in result:
        result[result.index('2')] = 'Silver Medal'
    if '3' in result:
        result[result.index('3')] = 'Bronze Medal'
    return result

if __name__ == '__main__':
    print(solution([123123,11921,1,0,123]))