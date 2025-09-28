from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):      
            group = arr[i:i+3]
            if all(num % 2 == 1 for num in group): 
                return True
        return False
