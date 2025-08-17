class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Reverse Traversal Method
        # if len(nums) == 0:
        #     return 0
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i] == val:
        #         nums.pop(i)
        # return len(nums)

        #Forward Traversal with variable Method
        # insertIndex = 0 
        # for i in range (len(nums)):
        #     #Check if you value is the nums[i]
        #     if nums[i] != val:
        #         nums[insertIndex] = nums[i]
        #         insertIndex += 1
        # return insertIndex
