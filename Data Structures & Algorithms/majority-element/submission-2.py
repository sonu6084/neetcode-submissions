class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_dict = {}
        for i in nums:
            majority_dict[i] = 1 + majority_dict.get(i,0)

        major_element = 0
        freq = 0
        for i in majority_dict:
            if majority_dict[i] > freq:
                major_element = i
                freq = majority_dict[i]

        return major_element