class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequent = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        res = []
        

        for n, c in count.items():
            frequent[c].append(n)
        
        print(frequent)

        for i in range(len(frequent)-1,0,-1):
            for j in frequent[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res