# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def technical(node):
            stk = [node]
            res = []
            while stk:
                x = stk.pop()
                if x.left:
                    stk.append(x.left)
                if x.right:
                    stk.append(x.right)
                if not x.left and not x.right: #leaf node
                    res.append(x.val)
            return res

        return technical(root1) == technical(root2)