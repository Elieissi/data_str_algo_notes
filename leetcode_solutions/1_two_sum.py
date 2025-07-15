class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for numb in range(len(nums)):
            for num in range(numb+ 1, len(nums)):
                if (nums[numb] + nums[num]) == target:
                    return [numb,num]