from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_sum(nums: List[int]) -> int:
            result = 0
            for num in nums:
                result ^= num
            return result
        n = len(nums)
        result = 0
        
        for i in range (1 << n):
            subset = [nums[j] for j in range(n) if (i & (1 << j))] 
            result += xor_sum(subset)
        
        return result
        
        
if __name__ == "__main__":
    test_cases = [
        {
            "nums": [1,3],
            "expected": 6
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        nums = test_case.get("nums")
        expected = test_case.get("expected")
        result = solution.subsetXORSum(nums)
        print(result, expected)