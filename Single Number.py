class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        x=Counter(nums)
        for i in x:
            if x[i]==1:
                return i
