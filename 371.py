# sum of two integers
# but you cannot use the operator + or -

def solution(a, b):
    sum1 = a^b
    sum2 = (a&b)<<1
    mask = 0xffffffff
    while sum2 != 0:
        sum1, sum2 = sum1^sum2, (sum1&sum2)<<1
        sum1 &= mask
        sum2 &= mask
    return sum1 if a > 0 or b > 0 else (~sum1)^mask

if __name__ == '__main__':
    print(solution(-1,-1))