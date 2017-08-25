# reverse words in a string

def reverse_words(s):
    words = s.split(' ')
    result = []
    for i in words:
        result.append(i[::-1])
    return ' '.join(result)

if __name__ == '__main__':
    print(reverse_words("Let's take LeetCode contest"))