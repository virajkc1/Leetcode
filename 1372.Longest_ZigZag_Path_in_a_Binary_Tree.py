# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path = 0 #this is to store longest path


        def dfs(node, left, curr): #we take a root node and we take a direction, left is True if coming from the left else false for Right
        #curr stores our current path

            #Our base case
            if node is None:
                return 
            self.path = max(self.path,curr) #after each recursion, we update self.path
            if left: #if we are coming from the left
                dfs(node.right,False, curr + 1) #the dfs you pass root.right, left is now False and current is +1
                dfs(node.left,True, 1) #if we are going left and were from left then we go back to setting our current back to 1
            else: #if left was False hence we were coming from right
                dfs(node.right,False,1) #then if we go to right again then our value is 1
                dfs(node.left, True, curr + 1) #else if we go left then our value is current +1
                #note that we have gone right then left as question states to do this
        
        #initialising at the roots
        dfs(root.right,False,1)
        dfs(root.left,True,1)

        #After self.path will be updated
        return self.path
#T:O(n) S:O(n)