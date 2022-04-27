# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# lenght of the string.

def urlfy(string, lenght):
    SPACE = ' '
    REPLACEMENT = "%20"
    new_string = ""
    if not isinstance(string, str) or not isinstance(lenght, int):
        return None
    for index in range(lenght):
        c = string[index]
        if c is SPACE:
            new_string += REPLACEMENT
        else:
            new_string +=c

    return new_string


assert urlfy("a b c", 5) == "a%20b%20c"
assert urlfy("a b c ", 5) == "a%20b%20c"
assert urlfy("a b c ", "3") is None
assert urlfy(2, 3) is None
assert urlfy(2, "3") is None
