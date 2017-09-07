# two sum

def solution(nums, target):
    temp = {}
    result = []
    for i in nums:
        if i in temp.keys():
            temp[i] += 1
        else:
            temp[i] = 1
    for i in temp.keys():
        t = target - i
        if t != i:
            if t in temp.keys():
                result.append(nums.index(i))
                result.append(nums.index(t))
                return result
            else:
                continue
        else:
            flag = nums.index(i)
            result.append(flag)
            nums[flag] -= 1
            result.append(nums.index(i))
            return result

if __name__ == '__main__':
    print(solution([2,7,8,8,11,15],16))