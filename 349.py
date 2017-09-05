# intersection of two arrays

def solution(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    result = []
    for i in nums2:
        if i in nums1:
            result.append(i)
    return result

if __name__ == '__main__':
    print(solution([1,2,3,4], [2,3]))
