# excel sheet column number

import math

def solution(s):
    result = 0
    for i in range(len(s)):
        result += (ord(s[i])-64)*math.pow(26, len(s)-i-1)
    return int(result)

if __name__ == '__main__':
    print(solution('AA'))