class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        soln = float("inf") # as we want the min value
        for r in range (0,len(nums)):
            summ += nums[r]
            while summ >= target:
                soln = min(soln,r-l+1)
                summ -= nums[l]
                l += 1
        return 0 if soln == float("inf") else soln
            

