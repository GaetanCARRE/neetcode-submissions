class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right, target):
            if left > right:
                return -1
            middle = (right - left) //2 + left
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                return binary_search(left, middle -1 , target)
            else:
                return binary_search(middle+1, right, target)
            return -1
    
        return binary_search(0, len(nums)-1, target)
