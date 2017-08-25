# reshape the matrix

def matrix_reshape(nums, r, c):
    if len(nums)*len(nums[0]) != r*c:
        return nums
    else:
        temp = []
        for i in nums:
            for o in i:
                temp.append(o)
        result = []
        for i in range(r):
            result.append(temp[i*c:i*c+c])
        return result

if __name__ == '__main__':
    print(matrix_reshape([[1,2],[3,4]], 2, 4))