class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)   #this converts the arrays in space to sets
        distinct_num1, distinct_num2 = (nums1 - nums2), (nums2 - nums1) #this is difference between sets
        answer = [list(distinct_num1),list(distinct_num2)] #converts them into lists & defined in an array called answer
        return answer #this returns the answer
    