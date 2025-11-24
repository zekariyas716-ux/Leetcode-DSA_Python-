class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0] * (len(gain) + 1)
        altitude[0] = 0
        for i in range(1,len(gain) + 1):
            altitude[i] = gain[i-1] + altitude[i-1]
        return max(altitude)    



