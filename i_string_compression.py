# Implement a method to perform a basic string compression using the counts
# of repeated characters. For example, the string aabbcccccaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return
# the original string. You can asume the string has only uppercase and lowercase letters (a - z)


def compress(string):
    if not isinstance(string, str):
        return False

    compressed = ""
    lastCompression = []
    compressionCount = {}

    for index, character in enumerate(string):
        if index == 0:
            compressed += character
            lastCompression[0] = character
            compressionCount[character] = 0
        else:
            if character in compressionCount:
                compressionCount[character] += 1
            else:
                compressionCount[character] = 0

            if character in lastCompression:
                
            else:
                compressed += character
            lastCompression = [character]

    print(compressed)

    return compressed


assert compress("aabbcccccaa") == "a2b1c5a3"
assert compress("aabbaa") == "a1b1a3"
assert not compress(1)
