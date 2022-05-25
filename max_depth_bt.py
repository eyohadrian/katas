def maxDepth(root: Optional[TreeNode]):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
