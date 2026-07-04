class Solution:

    def encode(self, strs: List[str]) -> str:
        separator = "#"
        global_string = ""
        for s in strs:
            global_string += f"{len(s)}{separator}{s}"

        return global_string


    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            number = ""
            while s[i] != "#" and i < len(s):
                number += s[i]
                i+=1
            num = int(number)
            result.append(s[i+1:i+1+num])
            i = i+1+num

        return result
