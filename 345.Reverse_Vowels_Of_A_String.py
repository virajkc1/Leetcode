class Solution:
    def reverseVowels(self, s: str) -> str:
        myVowelSet = set("aeiouAEIOU")
        #Set of vowels to search through in 0(1) Time
        myArr = list(s) #Converts the string into an array
        l = 0 # sets the left pointer at 0
        r = len(myArr) - 1 #sets the right pointer at end of the array
        while l < r: #while they dont cross
            if (myArr[l] in myVowelSet) and (myArr[r] in myVowelSet):
                #if the value at myArr l and at myArr r is in the vowelSet
                myArr[l], myArr[r] = myArr[r], myArr[l] #swaps them around
                l += 1
                r -= 1
            elif myArr[l] in myVowelSet: #if just the left element is then the right moves across
                r -= 1
            elif myArr[r] in myVowelSet:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(myArr)
            
            
