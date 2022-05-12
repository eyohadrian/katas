# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


def isValid(s):
    brackets = {'}':'{', ')': '(', ']': '['}
    stack = []

    for bracket in s:
        if bracket in brackets:
            if len(stack) > 0:
                last_bracket = stack.pop()
                if last_bracket != brackets[bracket]:
                    return False
            else:
                return False
        else:
            stack.append(bracket)

    return True if len(stack) == 0 else False


assert isValid("()") is True
assert isValid("(){}}{") is False

