# maximum swap

def solution(num):
    num = str(num)
    i = len(num)-1
    max = -1
    max_index = -1
    while i >= 0:
        if num[i] > max:
            max = num[i]
            max_index = i
        if max == 9:
            break
        i -= 1
    if max > num[0] and max_index != 0:
        return int(num[max_index]+num[1:max_index]+num[0]+num[max_index+1:])
    else:
        return int(num)

if __name__ == '__main__':
    print(solution(1))