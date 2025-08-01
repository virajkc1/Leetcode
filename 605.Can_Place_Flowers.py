class Solution
    def canPlaceFlowers(self, flowerbed List[int], n int) - bool
        f = [0] + flowerbed + [0]  #creating a new flowerbed with 0 at the start and end of the array so you can capture edge cases

        for i in range(1,len(f) - 1) #starting from index 1 to the second last element in the new f array
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0 #check if all the elements are 0
                f[i] = 1 #adding flowers when you have found a free spot in the array
                n -= 1 #reducing n by 1 each time
        return n = 0  #this will return either true or false