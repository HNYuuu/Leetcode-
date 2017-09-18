# longest palindrome

def solution(s):
    if s == '':
        return 0
    temp_dict = {}
    for i in s:
        if i not in temp_dict.keys():
            temp_dict[i] = 1
        else:
            temp_dict[i] += 1
    temp_odd = filter(is_odd, temp_dict.values())
    sum_odd = sum(temp_odd)-len(temp_odd)+1 if len(temp_odd) > 0 else 0
    sum_even = sum(filter(is_even, temp_dict.values()))
    return sum_even+sum_odd

def is_odd(x):
    return x % 2 == 1

def is_even(x):
    return x % 2 == 0

if __name__ == '__main__':
    print(solution('"civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"'))