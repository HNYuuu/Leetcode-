# distribute candies
# use 'set'

def distribute_candies(candies):
    candies_set = set(candies)
    candies_kind = len(candies_set)
    return candies_kind if candies_kind < len(candies)/2 else len(candies)/2

if __name__ == '__main__':
    print(distribute_candies([1,1,1,1]))