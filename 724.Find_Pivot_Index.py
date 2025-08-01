class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefixArr = [0] #T:0(N) SPACE:O(1)
        # for i in range(len(nums)): #builds the prefix array
        #     prefixArr.append(nums[i] + prefixArr[i])

        # postfixArr = [0] * (len(nums) + 1)  # so there are 7 0's
        # for i in range(len(nums) - 1, -1, -1): #goes from 5 to 0, -1 is not included, & 6 is not included goes from 5,4,3,2,1,0
        #     postfixArr[i] = postfixArr[i + 1] + nums[i] 
        #     #iteration 1: postfix[5] = postfix[6] + nums[5] which equals 6
        #     #iteration 2: postfix[4] = postfix[5] + nums[4] which equals 11

        
        # for i in range(len(nums)):
        #     if prefixArr[i] == postfixArr[i + 1]:
        #         return i
        # return -1

        #SOLUTION 2
        left_sum = 0 #sum of the left side set to be zero
        right_sum = sum(nums) #sum of the right side
        for i in range(len(nums)): # loop till the length of the nums
            right_sum -= nums[i] #decrement i from right_sum
            if left_sum == right_sum: #if they are both equal, return i
                return i
            left_sum += nums[i] #increment left_sum with i after loop
        return -1 #if unable to find the index, return -1