import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Produce a maximum heap firstly
        #Make all numbers negative so it makes a min heap and then reciprocal will be the maximum 
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
    
        heapq.heapify(nums) #this produces the minimum heap tree
        x = 0
        for j in range(k):
            x = -heapq.heappop(nums)
            # heapq.heapify(nums) DONT NEED TO HEAPIFY AGAIN AS HEAPPOP does it for you

        return x
            

