# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solve(l1: ListNode, l2: ListNode) -> ListNode:
    """ 待定 其他方法更好"""
    def dfs(l, r, i):
        if not l and not r and not i:
            return
        res = (l.val if l else 0) + (r.val if r else 0) + i
        node = ListNode(res % 10)
        node.next = dfs(l.next if l else None, r.next if r else None, res//10)
        return node
    return dfs(l1, l2, 0)


def gen(lt: list) -> ListNode:
    p = cur = ListNode(lt.pop(0))
    while lt:
        cur.next = ListNode(lt.pop(0))
        cur = cur.next
    return p


def print_lsitnode(res: ListNode):
    lt = []
    while res:
        lt.append(res.val)
        res = res.next
    print(*lt, sep='->')
    return


if __name__ == "__main__":
    l1 = gen([1, 6, 6, 5])
    l2 = gen([2, 4, 3])
    print_lsitnode(l1)
    print_lsitnode(l2)
    res = solve(l1, l2)
    print_lsitnode(res)
