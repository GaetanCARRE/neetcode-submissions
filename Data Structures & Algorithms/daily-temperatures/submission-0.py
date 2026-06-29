class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
                continue
            
            
            while stack and temp > stack[len(stack)-1][1]:
                temp_idx, _ = stack.pop()
                result[temp_idx] = i - temp_idx
            stack.append((i, temp))
        return result


