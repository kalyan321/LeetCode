# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=temp=ListNode(0)
        carry=0
        while(l1 or l2 or carry):
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            temp.next=ListNode(carry%10)
            temp=temp.next
            carry //=10
        return head.next