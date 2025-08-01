class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # My SOLUTION  T:O(n^2) 
        # result =[]
        # n = len(candies)
        # for i in range(0,n):
        #     count = True 
        #     for j in range(0,n):
        #         if (candies[i] + extraCandies) < candies[j]:
        #             count = False
        #             break
        #     result.append(count)
        # return result
        # MODEL T:O(n) if you run 2 separate for loops
        # k=max(candies) #Biggest number
        # n=len(candies)  #Len of the array
        # result=[] 
        # for i in range(n):  # loops array and adds extraCandies to all elements
        #     candies[i]+=extraCandies  #THIS IS INPLACE ARRAY MUTATION
        # for i in range(n):  #LOOPS AGAIN
        #     if candies[i]>=k:  #CHECKS IF THE MUTATED ARRAY IS GREATER THAN THE MAX CANDIES AT ANY POINT
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result


        #BEST SOLUTION IS WITH 1 FOR LOOP
        maximum = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= maximum:
                res.append(True)
            else:
                res.append(False)

        return res