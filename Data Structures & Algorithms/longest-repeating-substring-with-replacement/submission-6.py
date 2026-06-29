class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0 
        max_res = 0
        alphabet_map = {s[0] : 1}
        max_frequency = 1 
        while end < len(s):
            1
            if max_frequency + k >= end - start + 1:
                max_res = max(max_res, end - start + 1)
                end += 1
                if end >= len(s):
                    break
                if s[end] in alphabet_map:
                    alphabet_map[s[end]] += 1
                    if alphabet_map[s[end]] > max_frequency:
                        max_frequency = alphabet_map[s[end]]
                else:
                    alphabet_map[s[end]] = 1
            else:
                alphabet_map[s[start]] -= 1
                start+=1

        return max_res
