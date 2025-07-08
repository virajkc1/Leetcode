class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 #set your indexes
        r = len(height)-1 #right index at the end
        res = float("-inf") #result is a value as low as possible
        while l <= r: # checks while left is not > than right, so left is smaller
            width = r - l # this is the width 
            if height[l] <= height[r]: #checks if the height is smaller at l
                area = height[l] * width #calcs the area
                l += 1
            else: #if height is smaller at right side then area taken with that value
                area = height[r] * width
                r -= 1 #decrements
                #check its next index
            res = max(res,area) #after each area is calculated its checked with the min
 
        return res