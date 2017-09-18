# roman to integer

def solution(s):
    if s == "":
        return 0
    result = 0
    map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    i = 0
    while i < len(s):
        if s[i] == 'I':
            if i < len(s)-1 and s[i+1] != 'I':
                result += (map[s[i+1]]-1)
                i += 2
            else:
                result += 1
                i += 1
        elif s[i] == 'X':
            if i < len(s)-1 and s[i+1] != 'I' and s[i+1] != 'V' and s[i+1] != 'X':
                result += (map[s[i+1]]-10)
                i += 2
            else:
                result += 10
                i += 1
        elif s[i] == 'C':
            if i < len(s)-1 and (s[i+1] == 'D' or s[i+1] == 'M'):
                result += (map[s[i+1]]-100)
                i += 2
            else:
                result += 100
                i += 1
        else:
            result += map[s[i]]
            i += 1
    return result

if __name__ == '__main__':
    print(solution('CIX'))