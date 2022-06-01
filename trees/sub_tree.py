def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root:
        return False

    if root.val == subRoot.val:
        is_same_tree = isSameTree(root, subRoot)
        if is_same_tree:
            return is_same_tree

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(a, b):
    if not a and not b:
        return True

    if not a or not b or a.val != b.val:
        return False

    return True and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
