# find unique character in a string

def solution(s):
    temp_set = {()}
    temp_list = []
    for i in s:
        if i not in temp_set:
            temp_set.add(i)
            temp_list.append(i)
        else:
            if i in temp_list:
                temp_list.remove(i)
    if len(temp_list) == 0:
        return -1
    else:
        return s.index(temp_list[0])

if __name__ == '__main__':
    print(solution("aaddaad"))