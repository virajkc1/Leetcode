class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict #all values set to 0
        d = defaultdict(int)
        pairs = 0
        for num in nums:
            if d[k-num] > 0: #if we at a number and k - that number is present then its quantity is greater than 1
            #thats what we are checking or
                pairs += 1 #we can make a pair
                d[k-num] -= 1 #decrease that quantity by 1 from the dict
            else:
                d[num] += 1 #meaning we add it into there
        return pairs
