# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = ListNode(0)
        pre.next = head
        cur = pre.next
        while cur.next and cur.next.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        if cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val

        return pre.next

if __name__ == "__main__":
    head = ListNode(1)
    pre = head.next = ListNode(2)
    pre.next = ListNode(3)
    pre = pre.next
    pre.next = ListNode(4)
    Solution().swapPairs(head)
