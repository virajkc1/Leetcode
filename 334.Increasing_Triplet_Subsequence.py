class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #initialise the variables
        nums_i = float('inf') #need to be as big as possible

        nums_j = float('inf')
        for num in nums: #iterate thru all numbers
            if num <= nums_i: #if number is <= nums_i
                nums_i = num
            elif num <= nums_j:
                nums_j = num
            else:
                return True
        
        return False

