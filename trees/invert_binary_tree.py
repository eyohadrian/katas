def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    root.left  = self.invertTree(root.left)
    root.right = self.invertTree(root.right)

    return root
