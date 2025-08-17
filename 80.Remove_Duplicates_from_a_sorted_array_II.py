class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #2 Pointers solution with forward traversal
        # j = 1
        # count = 1
        # n = len(nums)
        # for i in range(1,n):
        #     if nums[i] == nums[i-1]:
        #         count += 1
        #     else:
        #         count = 1
            
        #     if count <= 2:
        #         nums[j] = nums[i]
        #         j += 1

        # return j

        #2 Pointers Solution
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k=k+1
        return k
