# Implement an algorithm to determine if a string has all unique characters

def algorithm(string):
    if not isinstance(string, str):
        return False

    characters = set()
    for c in string:
        if c in characters:
            return False
        else:
            characters.add(c)
    return True




assert algorithm("abc")
assert not algorithm("aba")
assert not algorithm(1)
