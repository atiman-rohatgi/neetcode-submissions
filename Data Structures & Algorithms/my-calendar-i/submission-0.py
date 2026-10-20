class MyCalendar:
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
    """
    - we can start by creating a list of pairs
    - whenever book function is called, any event can be booked either before or after the ones already there
    - so we compare the current event to one before and one after
    - before is 
    - we find the spot using binary search - (log n)
    - complexity
        - time = (n log n)
        - space = O(n)
    """
    
    def __init__(self):
        #initiializing a list
        self.calender = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        #binary search to find the inserting index
        left, right = 0, len(self.calender)
        while left < right:
            mid = (left+right) // 2
            if self.calender[mid][0] <= startTime:
                left = mid+1
            else:
                right = mid

        idx = left

        #check the rules for inserting on that index
        #previous element
        if idx > 0 and startTime < self.calender[idx-1][1]:
            return False
        #next element
        if idx < len(self.calender) and endTime > self.calender[idx][0]:
            return False
        #otherwsie insert
        self.calender.insert(idx, [startTime, endTime])
        return True
        