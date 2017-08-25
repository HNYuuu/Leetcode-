# judge circle, count the operations

def judge_circle(moves):
    ver_num, hor_num = 0, 0
    for i in moves:
        if i == 'U':
            ver_num += 1
        elif i == 'D':
            ver_num -= 1
        elif i == 'L':
            hor_num -= 1
        else:
            hor_num += 1
    if ver_num == 0 and hor_num == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(judge_circle('UDLRUDLRL'))

