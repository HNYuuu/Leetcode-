# two sum II

def solution(numbers, target):
    back_p, front_p = len(numbers)-1, 0
    while True:
        if numbers[back_p] + numbers[front_p] > target:
            back_p -= 1
        elif numbers[back_p] + numbers[front_p] < target:
            front_p += 1
        else:
            return [front_p+1, back_p+1]

if __name__ == '__main__':
    print(solution([2,7,11,19], 9))