from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = {k:[] for k in range(1,len(nums)+1)} 
        for key in c:
            v = c[key]
            # if not v in res:
            #     res[v]
            res[v].append(key)
        print(res)

        output = []
        rest = k
        for i in range(len(nums), 0, -1):
            if res[i] and rest:
                for r in res[i]:
                    output.append(r)
                    rest -= 1
                    if rest == 0:
                        print(f"breaking with {output}")
                        break
        
        return output