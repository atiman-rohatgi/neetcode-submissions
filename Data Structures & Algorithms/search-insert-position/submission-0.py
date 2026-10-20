class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        - we will do binary search
        - the main algo would check curr index -1 and +1 with the target
        - or if one side has nothing, like its the end
        """
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if left == right:
                return left
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1 
            else:
              right = mid  


        