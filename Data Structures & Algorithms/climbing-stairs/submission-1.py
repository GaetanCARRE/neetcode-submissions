class Solution:
    def climbStairs(self, n: int) -> int:
        # find the max for each n and reuse it to calculate the new size
        if n < 3:
            return n
        stairs = [-1]*(n+1)
        stairs[1] = 1
        stairs[2] = 2
        for i in range(3,n+1):
            print(i)
            stairs[i] =  stairs[i-1] + stairs[i-2]
        
        return stairs[n]





