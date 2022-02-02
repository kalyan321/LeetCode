# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def mainTreeTraversal(root):
            if root != None:
                self.mainTree.append(root.val)
            else:
                self.mainTree.append(None)
                return
            mainTreeTraversal(root.left)
            mainTreeTraversal(root.right)

        def subTreeTraversal(root):
            if root != None:
                self.subTree.append(root.val)
            else:
                self.subTree.append(None)
                return
            subTreeTraversal(root.left)
            subTreeTraversal(root.right)
        
        self.mainTree = []
        self.subTree = []
        subTreeTraversal(subRoot)
        mainTreeTraversal(root)
        n = len(self.mainTree)
        m = len(self.subTree)
        i = 0
        j = 0
        while i < n and j < m:
            if self.mainTree[i] == self.subTree[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            else:
                i = i - j + 1
                j = 0
        return False