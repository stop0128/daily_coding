from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count

if __name__ == "__main__":
    test_cases = [
        {
            "nums" : [1, 2, 3, 4],
            "k" : 2,
            "expected" : 0
        },
        {
            "nums" : [3, 1, 2, 2, 2, 1, 3],
            "k" : 2,
            "expected" : 4
        }
    ]
    for test_case in test_cases:
        nums = test_case["nums"]
        k = test_case["k"]
        expected = test_case["expected"]

        solution = Solution()
        result = solution.countPairs(nums, k)
        print(f"Test case passed: {test_case}")
        print(f"Result: {result}, Expected: {expected}")