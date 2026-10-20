class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the min as pivot
        l = 0
        r = len(nums) - 1
        mid = (l+r) // 2

        while l < r:
            if nums[mid] < nums[r]:
                r = mid
                mid = (l+r) // 2
            elif nums[mid] > nums[r]:
                l = mid+1
                mid = (l+r) // 2
        pivot = mid #this is the min value

        #binary search algo
        def binary_search (lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        #deciding which half to binary seach upon
        n = len(nums)
        if pivot == 0: #no rotation
            return binary_search(0, n-1)
        elif target >= nums[pivot] and target < nums[n-1]: #within the right half
            return binary_search(pivot, n-1)
        else: #within the lef thalf
            return binary_search(0, pivot -1)
            
