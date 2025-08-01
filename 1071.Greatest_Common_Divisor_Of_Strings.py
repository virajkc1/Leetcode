class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2) #this is the length of the 2 strings

        def isDivisor(wordLength):
            if (len1 % wordLength) or (len2 % wordLength): #meaning if either word is none zero with the length of smallest word, then it is not a factor so return False
                return False
            f1, f2 = len1 // wordLength, len2 // wordLength #f means factor 
            return str1[:wordLength] * f1 == str1 and str1[:wordLength] * f2 == str2 #checking can the original word be built back up with those strings

           
        for wordLength in range(min(len1, len2),0,-1):  #checks if len1 or 2 smaller and iterates by smaller number
            #for loop iterates fron max length of the smaller word then goes down 
            #because we want to check if big word is first divisible by the whole word then by 1         less char then 2 less characters etc.
            if isDivisor(wordLength): #this helper function has to return true
                return str1[:wordLength] 
        return "" #if you dont find it then return empty string
