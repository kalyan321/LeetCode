# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        maxi = float('-inf')
        for i in range(len(l)//2):
            maxi = max(maxi, l[i] + l[-1-i])
        return maxi