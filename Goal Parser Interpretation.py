class Solution:
    def interpret(self, command: str) -> str:
        result = command.replace("()","o").replace("(al)","al")
        return result
