class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split()
        for words in result:
            x = len(result[-1])
        return x    
