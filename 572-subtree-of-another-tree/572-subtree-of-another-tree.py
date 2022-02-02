# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def mainTreeTraversal(root, arr):
            if root != None:
                arr.append(root.val)
            else:
                arr.append(None)
                return
            mainTreeTraversal(root.left, arr)
            mainTreeTraversal(root.right, arr)
            return arr
        
        sub = mainTreeTraversal(subRoot, [])
        main = mainTreeTraversal(root, [])
        n = len(main)
        m = len(sub)
        i = 0
        j = 0
        while i < n and j < m:
            if main[i] == sub[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            else:
                i = i - j + 1
                j = 0
        return False