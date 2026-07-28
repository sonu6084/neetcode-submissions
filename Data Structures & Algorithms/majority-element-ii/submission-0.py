class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1 = None
        maj2 = None
        count1 = 0
        count2 = 0

        for n in nums:
            if maj1 == n:
                count1 += 1
            elif maj2 == n:
                count2 += 1
            elif count1 == 0:
                maj1 = n
                count1 += 1
            elif count2 == 0:
                maj2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0
        res = []
        for i in range(len(nums)):
            if maj2 == nums[i]:
                count2 += 1
            elif maj1 == nums[i]:
                count1 += 1

        if count1 > len(nums)/3:
            res.append(maj1)

        if count2 > len(nums)/3:
            res.append(maj2)

        return res

