from collections import deque
class Solution:
    # def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    #     q = deque([(root, 1)]) #a queue with the root initialised into it 
    #     res = float("-inf") #initialise the result at negative infinity
    #     return_level = 0

    #     while q:
    #         level_sum = 0
    #         level = 0
    #         for i in range(len(q)):
    #             node, level = q.popleft()
    #             if node: level_sum += node.val
    #             if node.left: q.append((node.left,level+1))
    #             if node.right: q.append((node.right,level+1))

    #     #now check the sums
    #         if level_sum > res:
    #             res = level_sum
    #             return_level = level
        
    #     return return_level

#FASTER BFS SOLUTION
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val #first the maxSum is the root value
        resDepth = 1 #at level 1 so result is 1 

        queue = deque([root]) #then pass the root into the queue
        depth = 1 #set current depth as 1

        # Perform BFS
        while queue: #while nodes in the queue
            currSum = 0 #currentSum set to 0
            for i in range(len(queue)):  # Iterate through nodes in the current level
                node = queue.popleft() #pops (FIFO) from the queue 
                currSum += node.val #the currentSum is accumulated
                if node.left: #adds the child elements onto the queue
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update maximum sum and result level
            if currSum > maxSum:
                maxSum = currSum
                resDepth = depth
            
            # Move to the next level
            depth += 1

        return resDepth

        #should note that: after 1 is popped you added q = [7,0] then you pop 7 and add its value to currentSum
        #currSum = 7, and you add the child elements on so q = [0,7,-8] 
        #you then take currentSum and the level and update if greater than the max so maxSum = 7 now
        # resDepth = 2, depth now becomes 3
        # q = [7,-8] note the queue gets bigger but at the start the length was 2 and then it grew to 3 but as for loop ALREADY called it was only going to loop the queue 2 times in that iteration
        #T:O(n)