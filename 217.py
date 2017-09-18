# contains duplicate

def solution(nums):
    return False if len(set(nums)) == len(nums) else True