class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Base Case Handling - if node does NOT EXIST
        # if not root:
        #     return None
        
        # #IF NODE IS P OR Q
        # if root == p or root == q:  #if the root is either p or q then u know the LCA stems from it so return the root
        #     return root
        
        # #RECURSION
        # l = self.lowestCommonAncestor(root.left,p,q) #else you call the function again and you pass the root as now the left child
        # r = self.lowestCommonAncestor(root.right,p,q)

        # #if l and r are Non Null  - so you FOUND BOTH TARGETS
        # #eg 5 and 1 are l and r then 3 is LCA
        # if l and r: 
        #     return root
        # else:
        #     return l or r #returns the next level
        #     #return the one that is defined, the one that isnt null 
        
        # #T: O(n) - 
        # S: O(1) - not defining any extra data structures, IF NOT COUNTING RECURSIVE STACK FRAMES ELSE IT WOULD BE O(n)
