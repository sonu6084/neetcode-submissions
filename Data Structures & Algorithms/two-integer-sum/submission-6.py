class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = dict()
        answer = []
        for i in range(len(nums)):
            if (target - nums[i]) in sum_dict:
                answer.append(sum_dict[target-nums[i]])
                answer.append(i)
            sum_dict[nums[i]] = i

        return answer