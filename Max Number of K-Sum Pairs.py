class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left,right = 0,len(nums)- 1
        while left < right:
            target = nums[left] + nums[right]
            if target == k :
                count += 1
                right -= 1
                left  += 1 
            elif target < k:
                left += 1
            else:
                right -= 1    
        return count        
