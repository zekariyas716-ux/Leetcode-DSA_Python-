from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        for i in count_t:
            if count_t[i] != count_s.get(i,0):
                return i      

