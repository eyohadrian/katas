class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if (not q and p) or (not p and q):
        return False
    if not p and not q:
        return True

    if p.val != q.val:
        return False

    leftSame = isSameTree(p.left, q.left)
    rightSame = isSameTree(p.right, q.right)

    return True and leftSame and rightSame

tree_3 = TreeNode(3)
tree_2 = TreeNode(2)
tree_1 = TreeNode(1, left=tree_2, right=tree_3)

print(isSameTree(tree_1, tree_1))
