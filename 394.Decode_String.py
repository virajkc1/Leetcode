class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] #using a stack , array list that is FILO

        for i in range(len(s)): #looping over the entire string
            if s[i] != "]": #if its NOT a closing bracket
                stack.append(s[i]) #add char into the stack
            else:
                substr ="" #have an empty substring, keep popping till at the opening bracket
                while stack[-1] != "[": #while the last item isnt an opening string
                    substr = stack.pop() + substr # we keep adding it to the start of the substring
                stack.pop() #pop again to remove the opening bracket
        # now need the integer, the value of k 
                k = ""
                while stack and stack[-1].isdigit(): #while the stack exists and we have a digit, python inbuilt function checks if a string is a digit if converted, we check latest item in the stack after the [ is popped
                    k = stack.pop() + k #add the number to the string
            #so if 34 then we first pop 4 so k = 4 then check next item which is 3 so then do 3 + k which is 34
        # so now we have our substring and number of times so add it back to the stack
                stack.append(int(k)* substr)
        return "".join(stack) # converts it from the list into a string

        #T: O(n)


            
        

