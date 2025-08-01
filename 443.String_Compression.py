class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0
        # we iterate the input and jump around when we have groups made
        while i < len(chars): # we use a while loop instead of a for loop
            group = 1 #check the length of each group
            while (group + i) < len(chars) and chars[group + i] == chars[i]:
            #check the index we checking inbounds AND
            #check that the index we are at is same as char at the index at i
                group += 1
            
            #now we know character and num times we seen it
            chars[insert] = chars[i] #insert will be the first element at the start
            insert += 1
            #put a number here if the group length is > 1, can be single or double digits
            if group > 1:
                #convert group as a string
                string = str(group)
                chars[insert:insert+len(string)] = list(string)
                #goes from position 1 to 1+ len of the group ( eg pos 1 to 3) takes up 1 and 2
                #we assigned these spaces the list version of string
                # eg string is "12" then list version is [1,2]

                #Now we have to move insert down
                insert += len(string) #bcos string length for 12 b's is 2 so it moves across those 2
            i += group # i moves over to the next group 
        return insert
