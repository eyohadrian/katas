def isBalanced(root):
    def x(root):
    if not root:
    return [True, 0]

        left = x(root.left)
        right = x(root.right)

        balanced = left[0] and right[0] and (True if abs(left[1] - right[1]) <= 1 else False)

        return [balanced, 1 + max(left[1], right[1])]

    return x(root)[0]
