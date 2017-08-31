# move zeroes

def solution(nums):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            i += 1
        else:
            nums.remove(nums[i])
            count += 1
    for i in range(count):
        nums.append(0)
    # 提交过程中不能有return
    return nums

if __name__ == '__main__':
    print(solution([0,0,1]))