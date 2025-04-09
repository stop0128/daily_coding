from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_of_nums = sum(nums)
        
        if sum_of_nums % 2 == 1:
            return False

        half_sum_of_nums = sum_of_nums // 2
        
        dp = [False] * (half_sum_of_nums + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(half_sum_of_nums, num-1, -1):
                if dp[i-num]:
                    dp[i] = True
        
        return dp[half_sum_of_nums]


if __name__ == "__main__":
    test_cases = [
        {
            "nums": [1,5,11,5],
            "expected": True
        },
        {
            "nums": [1,2,3,5],
            "expected": False 
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        nums = test_case.get("nums")
        expected = test_case.get("expected")
        result = solution.canPartition(nums)
        print(result, expected)