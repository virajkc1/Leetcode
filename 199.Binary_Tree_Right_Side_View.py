# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  #this is the result
        q = deque([root])  #initialise the queue with the root element

        while q: #while not empty, q has values in it
            rightSide = None #get rightSide element of the queue
            qLen = len(q) #length of the queue #get the length of the queue on a level
            #at start length is 1, 1 element on level 1

            for i in range(qLen): #loops one time after all the elements from a level are added
                node = q.popleft() #popping from the left (FIFO)
                if node: #if the node is not Null
                    rightSide = node #we update the rightSide var, its the 
                    q.append(node.left) 
                    q.append(node.right)
                
            if rightSide: #incase no nodes then you wont return initalised None
                res.append(rightSide.val) 
            
        return res
            #second iteration of the for loop
                # it has a q of 2 & 3
                #it will loop 2 times
                #
