class Solution:
    def reverseWords(self, s: str) -> str:
        #MY SOLUTION
        myArr = [i for i in s.split() if i.strip() != '']
        l = 0 
        r = len(myArr) - 1
        while l < r:
            myArr[l], myArr[r] = myArr[r], myArr[l]
            l += 1
            r -= 1
        return (" ".join(myArr)).strip()


        # BEST SOLUTION
        # strList = s.split(" ")
        # strList = filter(lambda word: word is not "", strList)
        # strList = list(strList)[::-1]
        # return " ".join(strList)
        