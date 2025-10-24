class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res =[]
        curr_index = 0
        space_index = 0
        while curr_index < len(s) :
            if space_index < len(spaces)and curr_index == spaces[space_index]:
                res.append(" ")
                space_index += 1
            res.append(s[curr_index])
            curr_index += 1
        return "".join(res)       
 
