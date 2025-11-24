class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        pivot_index = -1 
        for i in range(len(nums)):    
            left = 0 if i == 0 else prefix[i-1]
            right = prefix[-1] - prefix[i]
            if left == right:
                pivot_index = i
                break 
        return pivot_index

