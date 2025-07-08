class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        res, sol = [], [] #this makes an empty list of each, its always in backtracking qs
        #they are global empty lists
    
        def backtrack(i): #defined a function that takes an index
            if i == n: #this is immediately when our index goes out of bounds, at a base case
                res.append(sol[:]) #this means a solution copy, snapshot in time of what solution is storin
                return 
        
        #go down the left path, dont choose nums[i]
            backtrack(i+1)

        #Pick num at i
            sol.append(nums[i]) #temp pick it
            backtrack(i+1) 
            sol.pop() #to undo it we pop from the stack

        backtrack(0) #means we call the function to start at the first index
    #it then traverses the imaginary tree
    #then returns the result
        return res

    #Time: O(2^n) - doubling effect because of two branches 
    #Space O(h) where h is height of the tree, depth takes space because of recursion

