# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
## Input: s = "anagram", t = "nagaram"
## Output: true
# Example 2:
## Input: s = "rat", t = "car"
## Output: false
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def solution(A, B):
    if len(A) is not len(B):
        return False

    hash_map = {}

    for x in A:
        if x in hash_map:
            hash_map[x] += 1
        else:
            hash_map[x] = 1

    for x in B:
        if x in hash_map:
            hash_map[x] -= 1
            if hash_map[x] == 0:
                del hash_map[x]
        else:
            return False

    if len(hash_map) != 0:
        return False

    return True


assert solution("anagram", "nagaram") == True
assert solution("rat", "car") == False
