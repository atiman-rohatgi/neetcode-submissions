class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        - so basically we sort the cars to get started with the one with no obstacles
            - get the time = (target-pos)/speed
            - car behind it can be faster or slower
            - if faster they will evntually line up
            - if slower they wont line up hence fleet += 1
        - complexity
            - time = O(nlogn)
            - space = O(n)
        - 
        """

        #make a time dict
        times = {}
        for i in range(0, len(position)):
            times[position[i]] = (target-position[i]) / speed[i]

        #sort according to the position and get a times list
        times = dict(sorted(times.items(), reverse=True)) #descending
        times_list = list(times.values()) #convert the times into a list

        #count the number of fleet
        fleets = 0
        bottleneck = 0.0

        for time in times_list:
            if time > bottleneck:
                fleets += 1
                bottleneck = time
            else: #time <= bottleneck
                continue
            
        return fleets


            


        