# ransom note

def solution(ransomNote, magazine):
        r_dict, m_dict = {}, {}
        for i in ransomNote:
            if i not in r_dict.keys():
                r_dict[i] = 1
            else:
                r_dict[i] += 1
        for i in magazine:
            if i not in m_dict.keys():
                m_dict[i] = 1
            else:
                m_dict[i] += 1
        for i in r_dict.keys():
            if i not in m_dict.keys() or r_dict[i] > m_dict[i]:
                return False
        return True
        # a more efficient way
        # for i in set(ransomNote):
        #     if ransomNote.count(i) > magazine.count(i):
        #         return False
        # return True

if __name__ == '__main__':
    print(solution('aa', 'aab'))