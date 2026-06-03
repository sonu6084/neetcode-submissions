class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}

        if len(nums) == 0:
            return 0
        numset = sorted(set(nums))
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
        
        for i in numset:
            if i-1 in hashmap:
                hashmap[i]+=hashmap[i-1]


        return max(hashmap.values())