# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive DFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # check if left or right 
#         count = 0
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#Iterative BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         level = 0
#         q = deque([root]) #first node added to the queue
#         while q: #while it has something in it
#             for i in range(len(q)): #go through the queue
#                 #traversing through the level and popleft
#                 node= q.popleft()
#                 if node.left: #we never add null nodes to the queue so only works if we adding to the queue
#                     q.append(node.left) #add the node.left to the queue
#                 if node.right: #if node right then add it to the queue
#                     q.append(node.right)
#             level += 1 #first iteration you added 2 nodes (left and right ) and level becomes 1

# #next iteration is 2 times so it will pop both the elements it added from level 2 and add the children in, it will then increase the level to level 2
#         return level

#ITERATIVE DFS - PREORDER
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stk = [[root,1]] #we add the root and the Depth
        res = 0 #as we know we have at least 0
        while stk:
            node, depth = stk.pop()
            if node: #is not null
                res  = max(res,depth)
                stk.append([node.left, depth +1]) #we add both left and right to the stk but if its null then the if node statement will ignore it after its popped
                stk.append([node.right, depth+1])
        return res 

      