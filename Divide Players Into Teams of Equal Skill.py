class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right = 0 , len(skill)-1
        target = sum(skill)//(len(skill)//2)
        total_chem = 0
        while left < right :
            if skill[left] + skill[right] != target:
                return -1
            else:    
                total_chem += skill[left] * skill[right]
                right -= 1
                left +=1 
        return total_chem
