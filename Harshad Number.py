class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        lst = []
        for i in str(x):
            lst.append(int(i))
        total = sum(lst) 
        if x % total == 0 :
            return  total
        else:
            return -1
          
