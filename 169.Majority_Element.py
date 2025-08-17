class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # #Edge Case Testing
        # if len(nums) == 1:
        #     return nums[0]

        # #Variable Definition
        # finalCount = -(10**9)
        # tempCount = 1
        # val = -(10**9)

        # #Sorting of nums
        # nums.sort()

        # #Traversal
        # for i in range (1,len(nums)):
        #     #if same or different number
        #     if nums[i] == nums[i-1]:
        #         tempCount += 1
        #     else:
        #         tempCount = 1
            
        #     #now check the tempCount is greater than finalCount
        #     if tempCount > finalCount:
        #         val = nums[i]
        #         finalCount = tempCount
        # return val

        #Fastest way 
        #As its more than half, whichever element is in the half will always be the answer
        # nums.sort()
        # return nums[len(nums)//2]

        #Boyer-Moore Algorithm
        count = 0
        res = nums[0]

        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -=1
        return res
