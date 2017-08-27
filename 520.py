# detect capital

def detect_cap(word):
    if word.upper() == word: return True
    if word.lower() == word: return True
    if word[0].isupper() and word[1:].islower(): return True
    return False

if __name__ == '__main__':
    print(detect_cap('L'))