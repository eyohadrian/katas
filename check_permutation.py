# Given two strings, write a method to decide if one is a permutation of the other

def permutation(a, b):
    if not isinstance(a, str) or not isinstance(b, str):
        return False
    if len(a) is not len(b):
        return False

    hashmap = {}

    for character in a:
        if character in hashmap:
            hashmap[character] += 1
        else:
            hashmap[character] = 1
    for character in b:
        if character in hashmap:
            hashmap[character] -=1
        else:
            return False
    for _, counter in hashmap.items():
        if counter != 0:
            return False

    return True



# assert permutation("abc", "bca")
# assert not permutation("abc", "cbd")
# assert not permutation("a", "ab")
# assert not permutation(1, [1,2])
# assert permutation("a", "a")
assert permutation("1,2,3", "2,3,1")
