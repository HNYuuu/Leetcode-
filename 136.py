# single number
# use XOR

def single_number(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

if __name__ == '__main__':
    print(single_number([5,5,4]))