# assign cookies

def solution(g, s):
    if len(g) == 0 or len(s) == 0:
        return 0
    g.sort()
    s.sort()
    s_index, count, i = 0, 0, 0
    while i < len(g):
        if g[i] <= s[s_index]:
            count += 1
            i += 1
        s_index += 1
        if s_index == len(s):
            break
    return count

if __name__ == '__main__':
    print(solution([3,2,1], [1,2]))