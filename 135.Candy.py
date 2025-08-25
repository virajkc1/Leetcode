class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings)  # get an array of all 1's

        #First Pass - Left to Right
        for i in range (1,len(ratings)): # check the prior element to see if its the next avialable
            if ratings[i] > ratings[i-1]: 
                arr[i] = arr[i-1] + 1

        #Second Pass - Right to Left
        for j in range (len(ratings)-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                arr[j] = max(arr[j+1] + 1, arr[j])
        
        return sum(arr) 