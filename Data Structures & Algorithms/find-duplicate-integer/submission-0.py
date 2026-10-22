class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        - sorting will get us O(nlogn)
        - could use hash set, to track freq, will use O(n) space
        - seen set is also O(n)
        - always n+1, so we can jump to that index, also start from 0 actual index
        - we can use the nums to act as next index
        - we can use fast and slow pointer to detect cycle
        - then use 2 slow pointers to detect entry
        - complexity
            - time = O(n)
            - space = O(1)
        """

        #part1
        #use slow and fast
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        #part2
        #use slow and slow
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow