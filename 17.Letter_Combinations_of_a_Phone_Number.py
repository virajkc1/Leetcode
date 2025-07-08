class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #this is our base case 
        if len(digits) == 0:
            return []
        
        ans, sol = [], [] #2 global arrays, ans is the thing we return, sol will be all of the solutions dynamically so it shrinks and grows

        #Make a hashmap that goes from each digit - make it a string so if you iterate over the digits in the examples they are strings
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        #backtracking function
        n = len(digits)
        def backtrack(i=0):
        #starting at the first index
            if i == n:
                ans.append("".join(sol)) #sol is a list of strings that we can join up with no spaces to make 
                #add the solution to ans
                return 
            #if we are here then we didnt reach the end / not a base case

            for letter in letter_map[digits[i]]:
                #iterate through each of the characters of the value for each key
                #so if your key is 2 then iterate through abc
                #so letter would be a
                sol.append(letter) #using the letter 
                backtrack(i+1) #then move to the next letter & call it again so we eventually reach a base case
                sol.pop() #then we need to pop it off once all the backtrack recursion calls are over
            
        backtrack(0)
        return ans


