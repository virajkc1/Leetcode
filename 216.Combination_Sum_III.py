class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = [] #holds all the valid combos
        
        def backtrack(curr, k, n, start):
            #need current combo, k and n  and starting index so you know which elements to add past that element
            #1 is the base case , when do you stop
            # the other is when do you keep calling the function
            # you stop when k = 0 and n = 0 then you stop
            if k ==0 and n ==0:
                result.append(curr)
                return
            if k <= 0:
                return #you dont want to add any further elements after k reaches 0 
            #loop through all the numbers and try add to current combo
            for i in range(start,min(10,n+1)):
                #we can go up to and include 9 so use 10 as its exclsuive
                # if the combo is n = 4 then no point looping to 10 just go to 4 so n+1 so it includes the 4
                #loop all elements
                backtrack(curr +[i], k -1, n - i, i+1)
            return
        backtrack([],k,n,1)
        return result
        #T(9^k)
        # O(k) k is the depth of tree

                
