# longest uncommon subsequence
# it's a boring problem

def LUS(a, b):
    if a == b:
        return -1
    else:
        return max(len(a), len(b))