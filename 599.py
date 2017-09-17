# minimum index sum of two lists

def solution(list1, list2):
    list2_set = set(list2)
    result_dict = {}
    result = []
    for i in range(len(list1)):
        if list1[i] in list2_set:
            result_dict[list1[i]] = i+list2.index(list1[i])
    minimum = min(result_dict.values())
    for i in result_dict.keys():
        if result_dict[i] == minimum:
            result.append(i)
    return result

if __name__ == '__main__':
    print(solution(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))