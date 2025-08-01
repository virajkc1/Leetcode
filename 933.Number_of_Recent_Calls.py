class RecentCounter:

    def __init__(self):
        #initialise the queue because pop at the start
        self.times = deque()  #this is a queue for the number of pings

        

    def ping(self, t: int) -> int:
        self.times.append(t) #every time we call the ping function we add the time to self.times with the time
        while self.times and self.times[0] < t-3000: #while elements in the list and the start element is not in range
            self.times.popleft() #you pop from the left as its out the range
        #once you exit is everything that is valid
        #its the number of requests from t-3000 and t
        return len(self.times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

#S-0(1)
#t- 0(1) because if you get a ping every second then every new request you just remove 1 ping but if every 3000 seconds you still only remove 1 ping
#because of the range you wont always have an increasingly larger list of requests, there is a max hence its 0(1)