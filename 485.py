# max consecutive ones

def max_ones(nums):
    m_length = 0
    max = 0
    for i in nums:
        if i == 1:
            m_length += 1
            if max < m_length:
                max = m_length
        else:
            m_length = 0
    return max

if __name__ == '__main__':
    print(max_ones([1,1,0,1,1,1,0,0,1,1,1,1]))