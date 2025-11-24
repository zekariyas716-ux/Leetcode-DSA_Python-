class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        hm = {0:1}
        for i in nums:
            prefix += i
            if (prefix - k) in hm:
                count += hm[prefix- k]
            hm[prefix] = hm.get(prefix,0) +1
        return(count)        
