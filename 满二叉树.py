class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


x = map(int, input().strip().split(','))
x = list(x)
root = TreeNode(x.pop(0))    
res = [root]
while x:
    p = res.pop(0)
    if x:
        p.left = TreeNode(x.pop(0))
    else:
        break
    if x:
        p.right = TreeNode(x.pop(0))
    else:
        break
    res.append(p.left)
    res.append(p.right)

res = []
tmp = ''
flag = True
while res or root:
    while root:
        res.append(root)
        root = root.left
    root = res.pop()
    # print(root.val, end=' ')
    if tmp != '':
        if tmp > root.val:
            flag = False
        else:
            tmp = root.val
    else:
        tmp = root.val
    root = root.right
print(flag)