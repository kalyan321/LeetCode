# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def maxPairSum(head, i):
            if not head.next:
                return 0, head, 0
            count, node, res = maxPairSum(head.next, i + 1)
            if i <= count:
                res = max(res, node.val + head.val)
                return count + 1, node.next, res
            else:
                return count + 1, head, res
        return maxPairSum(head, 0)[2]