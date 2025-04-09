from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_of_nums = sum(nums)
        
        if sum_of_nums % 2 == 1:
            return False

        half_sum_of_nums = sum_of_nums // 2
        
        i, j = 0, 0
        while 1:
            sum_subset = sum(nums[i:j])
            if sum_subset > half_sum_of_nums:
                i += 1
            if sum_subset < half_sum_of_nums:
                j += 1
            if sum_subset == half_sum_of_nums:
                return True
            if i > n or j > n:
                return False
        
        return False


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