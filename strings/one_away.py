# There are three types of edits that can be performed on strings, insert a character, 
# removee a character or replace a character. Given Two strings write a function to check if they are one edit
# (or zero edits) away
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false


def one_away(text, mutated_text):
    if not isinstance(text, str) or not isinstance(mutated_text, str):
        return False

    text_table = {}
    mutated_table = {}

    for c in text:
        if c in text_table:
            text_table[c] += 1
        else:
            text_table[c] = 1
    
    for c in mutated_text:
        if c in mutated_table:
            mutated_table[c] += 1
        else:
            mutated_table[c] = 1

    differences = 0
    
    for c,total in text_table.items():
        if c in mutated_table:
            if mutated_table[c] != total:
                differences+=1
        else:
            differences+=1
    
    if differences <= 1:
        return True

    return False

assert one_away("pale", "ple")
assert one_away("pale", "pale")
assert one_away("pales", "pale")
assert one_away("pale", "bale")
assert not one_away("pale", "bake")
assert not one_away("xxx", 1)
assert not one_away(1, "xxx")
assert not one_away(1, 1)