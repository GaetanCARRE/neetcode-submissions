class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0 
        max_res = 0
        alphabet_map = {}
        while end < len(s):
            if not alphabet_map:
                alphabet_map[s[0]] = 1
            if self.max_map(alphabet_map) + k >= end - start + 1:
                max_res = max(max_res, end - start + 1)
                print(f"{max_res=}")
                end += 1
                if end >= len(s):
                    break
                if s[end] in alphabet_map:
                    alphabet_map[s[end]] += 1
                else:
                    alphabet_map[s[end]] = 1
            else:
                alphabet_map[s[start]] -= 1
                start+=1

        return max_res

    
    def max_map(self, alphabet_map: dict) -> int:
        max_v = 0
        for v in alphabet_map.values():
            max_v = max(max_v, v)

        return max_v


