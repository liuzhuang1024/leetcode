# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solve(l1: ListNode, l2: ListNode) -> ListNode:
    """ 待定 """
    p = pre = cur = ListNode(0)
    while l1 or l2:
        pass
    return p


def gen(lt: list) -> ListNode:
    p = cur = ListNode(lt.pop(0))
    while lt:
        cur.next = ListNode(lt.pop(0))
    return p


if __name__ == "__main__":
    l1 = [1, 2, 3]
    l2 = [2, 4]
    res = solve(gen(l1), gen(l2))
    print(res)
