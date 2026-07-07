class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0,0
        char_list = set()
        max_len = 0
        while end < len(s):
            if s[end] not in char_list:
                char_list.add(s[end])
                end += 1
            else:
                max_len = max(max_len, end - start)
                while s[end] in char_list:
                    char_list.remove(s[start])
                    start += 1

        max_len = max(max_len, end - start)
        return max_len     
        
                    


    