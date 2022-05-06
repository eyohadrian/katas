# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or a phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# You can ignore casing and non-letter characters.

# EXAMPLE

# Input: Tact Coa
# Output True (permutations: "taco cat", "atco cta", etc.)

def palindrome_permutation(text):
    if not isinstance(text, str):
        return False

    characters = {}

    text = text.strip()

    for c in text:
        if c != ' ':
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1

    odd = 0

    for _, total in characters.items():
        if total % 2 != 0:
            odd+=1

    if odd > 1:
        return False

    return True


# Palindrome: ette
assert palindrome_permutation("tete")
assert palindrome_permutation("teet")
assert palindrome_permutation("te et")

# Palindrome: Tact Coa
assert palindrome_permutation("taco cat")
assert palindrome_permutation("atco cta")
assert palindrome_permutation(" taco cat ")
assert not palindrome_permutation(" txcx  ceo ")

assert not palindrome_permutation("xaxaxa")
assert not palindrome_permutation("pipipopu")

assert not palindrome_permutation(12)
