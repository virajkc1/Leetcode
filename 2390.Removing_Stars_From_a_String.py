class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s: #loop over every star in s
            if char == "*":
                if stack: #meaning if its not empty
                    stack.pop() #removes the last character
            else:
                stack.append(char)
        return "".join(stack) #joins the stack up 
        #s = "*sta**r*s"
        """
        first the * wont pop from stack as nothing in it
        so it moves to next iteration
        s joins onto the stack
        then t then a 
        then a star is iterated over- checks the stack an "a" is first element 
        to be popped (FILO / LIFO) so its popped
        * is NEVER added to the stack just a marker for when to pop
        """
