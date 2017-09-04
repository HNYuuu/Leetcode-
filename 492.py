# construct the rectangle

import math

def solution(area):
    ini = int(math.ceil(math.sqrt(area)))
    # for i in range(ini, area+1):
    #     if area % i == 0:
    #         return [i, area/i]
    while ini <= area:
        if area % ini == 0:
            return [ini, area/ini]
        ini += 1

if __name__ == '__main__':
    print(solution(10000000))
