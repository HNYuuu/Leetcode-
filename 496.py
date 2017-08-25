# next greater element I
# important!

def next_greater_element(findNums, nums):
    reference = {}
    stack = []
    result = []
    for i in nums:
        while len(stack) and stack[-1] < i:
            reference[stack.pop()] = i
        stack.append(i)
    for i in findNums:
        result.append(reference.get(i, -1))
    return result

if __name__ == '__main__':
    print(next_greater_element([4,1,2], [1,3,4,2]))