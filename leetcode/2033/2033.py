from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        numbers = []
        result = 0 
        
        for row in grid:
            numbers.extend(row)
            
        if len(numbers) == 1:
            return 0
        
        numbers.sort()
        
        mid = len(numbers) // 2
        
        for number in numbers:
            abs_number = abs(number - numbers[mid])
            if abs_number % x != 0:
                return -1
            result += abs_number // x
        
        return result

if __name__ == "__main__":
    test_cases = [
        {
            "grid": [[2,4], [6,8]],
            "x": 2, 
            "expected": 4
        },
        {
            "grid": [[1,5], [2,3]],
            "x": 1,
            "expected": 5
        },
        {
            "grid": [[1,2], [3,4]],
            "x": 2,
            "expected": -1
        },
        {
            "grid": [[146]],
            "x": 86,
            "expected": 0
        },
        {
            "grid": [[931,128],[639,712]],
            "x": 73,
            "expected": 12
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        grid = test_case.get("grid")
        x = test_case.get("x")
        expected = test_case.get("expected")
        result = solution.minOperations(grid, x)
        print(result, expected)