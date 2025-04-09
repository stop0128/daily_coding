from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_nums = list(set(nums))
        sorted_nums = sorted(unique_nums)
        
        if k > sorted_nums[0]:
            return -1
        
        if k == sorted_nums[0]:
            return len(sorted_nums) - 1
        
        if k < sorted_nums[0]:
            return len(sorted_nums)
    

if __name__ == "__main__":
    test_cases = [
        {
            "nums": [5,2,5,4,5],
            "k": 2,
            "expected": 2
        },
        {
            "nums": [2,1,2],
            "k": 2,
            "expected": -1
        },
        {
            "nums": [9,7,5,3],
            "k": 1,
            "expected": 4
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        nums = test_case.get("nums")
        k = test_case.get("k")
        expected = test_case.get("expected")
        result = solution.minOperations(nums, k)
        print(result, expected)