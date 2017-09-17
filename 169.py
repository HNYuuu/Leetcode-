# majority element

def solution(nums):
    nums_set = set(nums)
    majority = len(nums)//2
    for i in nums_set:
        if nums.count(i) > majority:
            return i

if __name__ == '__main__':
    print(solution([1,2,2]))