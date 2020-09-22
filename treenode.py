class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def gen_tree(tree):
    """
    生成树结构
    """
    if not tree:
        return 
    root = cur = TreeNode(tree.pop(0))
    res = [cur]
    while tree:
        cur = res.pop(0)
        val = tree.pop(0)
        cur.left = TreeNode(val)
        res.append(cur.left)
        if tree:
            val = tree.pop(0)
            cur.right = TreeNode(val)
            res.append(cur.right)
    return root