# minimum moves to equal array elements

def solution(nums):
    return sum(nums) - min(nums) * len(nums)

if __name__ == '__main__':
    print(solution([1,200000000]))