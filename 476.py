# a easy String test

def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    bit_str = bin(num)[2:]
    result = []
    for i in bit_str:
        if i == '0':
            result.append('1')
        else:
            result.append('0')
    ''.join(result)
    return int(''.join(result), 2)

if __name__ == '__main__':
    print(findComplement(5))