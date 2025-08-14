class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Positioned at index  = 0 (2)
        Each element represents max jump length at that index 
        Eg: index = 1 (3)
            index = 2 (1)
            index = 3 (1)
            index = 4 (4)
        
        Return true if you can reach index at 4 so 4

        """
        goal = len(nums)  - 1 #Goal is set to the end
        for i in range(len(nums)-1,-1,-1): #last index 
            if i + nums[i] >= goal: #we can reach the goal
                goal = i
        
        #either goal is 0 or goal is greater than 0 then its false
        return True if goal == 0 else False