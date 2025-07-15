class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        set_nums = set(nums)

        return len(set_nums) != len(nums)   