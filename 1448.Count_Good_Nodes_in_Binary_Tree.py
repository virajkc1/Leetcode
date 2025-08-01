# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        stk=[(root,float("-inf"))] #for the root node it has a maximum on negative infinity, added tuple to the stack

        while stk:
            node, largest = stk.pop() #takes the node and the initial largest value popped 
            if largest <= node.val: #if the initial largest is smaller than the node value
                good_nodes += 1 #then we have a good node so increment it
            
            largest=max(largest,node.val) #regardless, we compare both the largest with node value to update the largest

            if node.right:
                stk.append((node.right,largest)) #if we have node.right then add it into the stack along with the current largest value
            
            if node.left:
                stk.append((node.left,largest))
            #Note that the order is NLR as stack is LIFO
        
        return good_nodes
        #Time Complexity: O(n) traversing through all of them
        #Space Complexity: O(n) as the stack will store n items

        #largest is a local variable as it changes for each nodes path, 