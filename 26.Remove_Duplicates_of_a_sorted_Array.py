class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Set Solution
        # seenSet = set()
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i] in seenSet:
        #         nums.pop(i)
        #     else:
        #         seenSet.add(nums[i])
        # return len(nums)

        #2 Pointers Solution
        l,r = 0,1
        while r < len(nums):
            if nums[l] != nums[r]:
                #you have a unique number
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1
        