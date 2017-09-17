# valid anagram

def solution(s, t):
    if s == "" and t == "":
        return True
    s_dict = {}
    for i in s:
        if i not in s_dict.keys():
            s_dict[i] = 1
        else:
            s_dict[i] += 1
    for i in t:
        if i in s_dict.keys():
            s_dict[i] -= 1
        else:
            return False
    if min(s_dict.values()) == 0 and max(s_dict.values()) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(solution("anagram", "nagaram"))