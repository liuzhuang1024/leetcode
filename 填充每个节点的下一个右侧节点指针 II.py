# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def gen_tree(lt):
    """ 生成树 """
    root = Node(lt.pop(0))
    res = [root]
    while lt:
        tmp = []
        for root in res:
            if lt:
                root.left = Node(lt.pop(0))
                tmp.append(root.left)
            if lt:
                root.right = Node(lt.pop(0))
                tmp.append(root.right)
        res = tmp
    return root


def solve(root):
    """ 层遍历 """
    if not root:
        return root
    p = root
    res = [root]
    while res:
        tmp = []
        for index, root in enumerate(res):
            if index < len(res)-1:
                root.next = res[index+1]
            else:
                root.next = None

            if root.left:
                tmp.append(root.left)
            if root.right:
                tmp.append(root.right)
        res = tmp

    return p


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, None, 7]
    root = gen_tree(lt)
    res = solve(root)
    print(res)
