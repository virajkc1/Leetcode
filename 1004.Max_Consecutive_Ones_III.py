class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        max_ones = 0
        while end < len(nums):
            if nums[end] == 0: #start, end start at 0
                k -=1 #if either at 0 then k decreases by 1
                
            
            while k < 0: # cant be less than 0
                if nums[start] == 0: 
                    k += 1 # k increases
                start += 1 #start moves up by 1 
                # so if start is at 0 or not it increases by 1


            max_ones=max(max_ones,end-start+1) #finds the max sequence
            end += 1 #outside if statement as we want end to increment each time if its at 0 or 1

        return max_ones