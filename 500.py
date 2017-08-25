def findWords(words):
    rule = ['QWERTYUIOPqwertyuiop', 'ASDFGHJKLasdfghjkl', 'ZXCVBNMzxcvbnm']
    flag = []
    result = 0
    result_words = []
    for i in words:
        for o in i:
            if o in rule[0]:
                result += 101
            elif o in rule[1]:
                result += 103
            else:
                result += 107
        flag.append(result)
        result = 0

    for i in range(len(flag)):
        if flag[i] % 101 == 0 or flag[i] % 103 == 0 or flag[i] % 107 == 0:
            result_words.append(words[i])
    return result_words

if __name__ == '__main__':
    print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
