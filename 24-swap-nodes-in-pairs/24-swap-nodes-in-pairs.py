# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(prev, head):
            if not head or not head.next:
                return head
            rec(head.next, head.next.next)
            if not head.next:
                return head
            print(prev.val, head.val)
            temp = head
            head = head.next
            temp.next = head.next
            head.next = temp
            prev.next = head
            return head
        prev = ListNode()
        prev.next = head
        return rec(prev, head)