# find the difference

def solution(s, t):
    s_sum, t_sum = 0, 0
    for i in s:
        s_sum += ord(i)
    for i in t:
        t_sum += ord(i)
    return chr(t_sum-s_sum)

if __name__ == '__main__':
    print(solution('abcd', 'abcde'))
