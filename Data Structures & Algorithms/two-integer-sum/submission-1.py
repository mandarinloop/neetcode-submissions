class Solution:
    def twoSum(self, nums: list[int], target:int) ->list[int]:
        n = len(nums)
        j = 0
        while (j <= n):
            for i in range(n):
                if nums[i] + nums[j] == target and i != j:
                    return [j, i]
            j = j + 1

        