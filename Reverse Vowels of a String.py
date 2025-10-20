class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ["A","E","I","O","U","a","e","i","o","u"]
        left,right =0,len(s) -1
        while left <= right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue
            s[right],s[left] = s[left],s[right]
            left += 1
            right -= 1
        return "".join(s)            
