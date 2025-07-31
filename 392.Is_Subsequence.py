class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0, 0
        s_len = len(s)
        t_len = len(t)

        while i < s_len and j < t_len:
            if s[i] == t[j]: # if they both match
                i += 1 # increment i 
            j += 1 # j will increment regardless
        
        return True if i == len(s) else False

        #i only increases if a match is found
        #you then check if i equals the len of s then all the characters are found
        #else you return False



