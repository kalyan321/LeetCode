# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        ans = []
        while queue:
            l = []
            for i in range(len(queue)):
                ele = queue.pop(0)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                l.append(ele.val)
            ans.append(l)
        return ans