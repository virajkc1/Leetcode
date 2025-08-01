# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root):
        #say we want to delete key 4 - we want to merge it together
        # if no left child
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        #if left and right exist 
        #get largest on left side and add the right side to it
        curr = root
        left = root.left
        right = root.right
        while left.right:
            left = left.right
        left.right = right
        return curr.left


        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #Edge cases 
        if not root:
            return None
        
        #Helper function 
        #root value is the key
        #takes left and right sub tree , merges them and returns the root
        if root.val == key:
            return self.helper(root) 
        
        curr = root
        while root: #if not on the key then search for it
            if key < root.val:  #need to search the left if less than the root value
                if root.left and root.left.val == key: #if left exists and root.left.val is the key
                #the root you are on will call helper
                    root.left = self.helper(root.left)
                    break
                root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                root = root.right

        return curr # we return the top root
