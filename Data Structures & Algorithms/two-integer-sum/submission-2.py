class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        rlist = []
        for i in range(0,len(nums)):
            if nums[i] in hashmap.keys():
                rlist.append(hashmap[nums[i]])
                rlist.append(i)
                return rlist
            else:
                hashmap[target-nums[i]] = i
            

       