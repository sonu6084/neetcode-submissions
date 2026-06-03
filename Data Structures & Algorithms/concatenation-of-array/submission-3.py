class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num1 = nums.copy()
        num2 = nums.copy()
        nums = num1 + num2
        return nums