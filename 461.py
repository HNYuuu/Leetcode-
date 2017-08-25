# hamming distance

def hamming_distance(x, y):
    x_str = bin(x)[2:]
    y_str = bin(y)[2:]
    len_max = max(len(x_str), len(y_str))
    x_str = x_str.zfill(len_max)
    y_str = y_str.zfill(len_max)
    count = 0
    for i in range(len(x_str)):
        if x_str[i] != y_str[i]:
            count += 1
    return count

if __name__ == '__main__':
    print(hamming_distance(1,4))