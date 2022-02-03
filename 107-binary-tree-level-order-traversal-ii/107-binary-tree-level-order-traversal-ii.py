# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        def preOrder(root, level):
            if root is None:
                return
            d.setdefault(level, []).append(root.val)
            preOrder(root.left, level + 1)
            preOrder(root.right, level + 1)
        preOrder(root, 1)
        ans = []
        for i in range(len(d), 0, -1):
            ans.append(d[i])
        return ans