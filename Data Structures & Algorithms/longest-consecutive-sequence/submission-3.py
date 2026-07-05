class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_set = set(nums)
        longest_serie = 0
        for num in numbers_set:
            if num-1 not in numbers_set: #beggining
                sequence_len = 1
                while num + 1 in numbers_set: 
                    sequence_len +=1
                    num += 1 
                longest_serie = max(sequence_len, longest_serie)
        
        return longest_serie