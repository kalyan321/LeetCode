# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        def recur(head):
            if head.next is None:
                return [0], [head.val]
            ans, stack = recur(head.next)
            while stack and stack[-1] <= head.val:
                stack.pop(-1)
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(0)
            return ans, stack + [head.val]
        return recur(head)[0][::-1]