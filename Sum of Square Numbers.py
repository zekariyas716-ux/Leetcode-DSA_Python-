class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(c**0.5)
        num = list(range(0,n+1))
        left,right = 0,len(num)-1
        while left <= right:
            summ = num[left]**2 + num[right]**2
            if summ == c:
                return True 
            elif summ < c:
                left += 1
            else:
                right -= 1           
        return False         
