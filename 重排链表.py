# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        cur = head
        while cur:
            end = cur
            while end.next and end.next != cur:
                end = end.next
            
            


        return head


if __name__ == "__main__":
    tmp = ListNode(4, ListNode(5))
    tmp = ListNode(3, tmp)
    tmp = ListNode(2, tmp)
    head = ListNode(1, tmp)

    Solution().reorderList(head)
