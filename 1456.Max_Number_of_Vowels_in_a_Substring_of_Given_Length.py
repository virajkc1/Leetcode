class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"} #a set of all your vowels
        curr = 0 #current count

        #this is your first fixed window of size 3
        for i in range(k): #runs through number indexes: 0 to k-1 (3)  hence 4 numbers
            if s[i] in vowels: #if any value in the first window is in vowels
                curr += 1 #current score increases by 1
        max_vowels = curr #the max_vowels is intialised

        for i in range(k,len(s)):  #loop from 3 to then rest of the string 
            if s[i] in vowels: #you will then loop to check next value is vowels
                curr += 1 #increasing current score - windwo size is 4 here
            if s[i-k] in vowels: #so removing the window to 3 and checking if vowel was here
                curr -= 1
        
            max_vowels = max(max_vowels,curr) #checks for the max

        return max_vowels