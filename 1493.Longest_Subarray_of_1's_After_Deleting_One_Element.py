class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        start = 0 #index 0
        zero = -1 #havent seen any zeros yet so assigned the index to -1
        for i in range(len(nums)): #iterate over the whole array
            if nums[i] == 0: #if index u are on is 0
                start = zero + 1 #move starting pointing AFTER the last occurence of a zero
                zero = i #update the last occurence of 0
            max_len = max(max_len, i - start)
            #comparing the max lengths, with current length
        return max_len