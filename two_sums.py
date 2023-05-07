from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i


if __name__ == "__main__":
    solution = Solution()
    x = solution.twoSum([2, 7, 11, 15], target=9)
    # x = solution.twoSum([3, 2, 3], target=6)
    print(x)

