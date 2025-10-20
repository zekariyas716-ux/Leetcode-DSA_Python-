class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats =0 
        left,right = 0,len(people) - 1
        while left <= right :
            summ = people[left] + people[right]
            if summ <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                if people[right] > people[left]:
                    boats += 1
                    right -= 1
                else:
                    boats += 1
                    left += 1         
        return boats
