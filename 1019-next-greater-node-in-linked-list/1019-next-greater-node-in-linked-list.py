# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        self.res = []
        def recur(head):
            if head.next is None:
                self.res.append(0)
                return [0], [head.val]
            ans, stack = recur(head.next)
            while stack and stack[-1] <= head.val:
                stack.pop(-1)
            if stack:
                self.res.append(stack[-1])
                ans.append(stack[-1])
            else:
                ans.append(0)
                self.res.append(0)
            return ans, stack + [head.val]
        s = recur(head)
        return(s[0][::-1])
        return self.res[::-1]