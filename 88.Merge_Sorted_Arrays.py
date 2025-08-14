class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        #MY VERY EASY SOLUTION
        # nums1[m:] = nums2
        # nums1.sort()
        # return nums1

        # Reverse iteration - While Loop solution
        # x = m - 1
        # y = n - 1
        # z = m + n - 1
        # while y >=0:
        #     #If num1 element has elements left and bigger
        #     if x >= 0 and nums1[x] > nums2[y]:
        #         nums1[z] = nums1[x] 
        #         x -= 1
        #     else:
        #         nums1[z] = nums2[y]
        #         y -= 1
        #     z-=1
        # return nums1

        #Reverse iteration - for loop solution
        x = m - 1
        y = n - 1
        for z in range((m+n-1),-1,-1):
            #Loops over every element once, backwards, in the nums1 loop

            #Check if x is not in range
            if x < 0:
                nums1[z] = nums2[y]
                y -=1

            #Check if y is not in range
            elif y < 0:
                break
            #Check nums1 < nums2
            #Both are now valid
            elif nums1[x] >= nums2[y]:
                nums1[z] = nums1[x]
                x -=1

            else:
                nums1[z] = nums2[y]
                y -=1
            

        return nums1
