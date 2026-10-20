class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        - iterate through the array
        - track the ones seen, as soon as 0 seen, reset the count
        - return max seen
        - complexity
            - time = O(n)
            - space = O(1)
        """
        
        count = 0
        mx = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
                mx = max(mx, count)
            else:
                count = 0

        return mx
