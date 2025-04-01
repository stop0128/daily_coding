from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n 
        
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
    
if __name__ == "__main__":
    test_cases = [
        {
            "nums": [-2,1,-3,4,-1,2,1,-5,4], 
            "expected": 6
        },
        {
            "nums": [1], 
            "expected": 1
        },
        {
            "nums": [5,4,-1,7,8], 
            "expected": 23
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        nums = test_case.get("nums")
        expected = test_case.get("expected")
        result = solution.maxSubArray(nums)
        print(result, expected)