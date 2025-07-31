class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1 #only have to go through the array once

        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            #get last index
            j = -i - 1
            #[1,2,3,4]
        #if   i     j
        #       i j
        #       j i
        #     j     i 
        # going forwards(i) and backwards at the same time
            l_arr[i] = l_mult # first l_mult holds one so first(furthest left element is 1)
            l_mult *= nums[i] #this is then replaced by the 1 * the number
            r_arr[j] = r_mult #this is set to 1
            r_mult *= nums[j] #then its set to 1 *nums[j]

            #2nd iteration
            #
            #
            #
            #
            #
            #

        return [l*r for l,r in zip(l_arr,r_arr)]

        #zip does this ([1, 2, 3], [4, 5, 6])  →  [(1, 4), (2, 5), (3, 6)]
# you then extract l & r in the pair, multiply them then return it into the array
        #iterate both arrays at the exact same time
        #each position in the new array is the multiplication of all the stuff that is to the left and right

        #T: 0(n) & S: O(n)
         





