from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_diff = float("inf")
        max_diff = float("-inf")
        sum_diff, count = 0, 0
        for difference in differences:
            sum_diff += difference
            if sum_diff <= min_diff:
                min_diff = sum_diff
            if sum_diff >= max_diff:
                max_diff = sum_diff
                
        for i in range(lower, upper+1):
            if ((min_diff + i) >= lower) and ((max_diff + i) <= upper):
                count += 1
                
        return count
    
if __name__ == "__main__":
    test_cases = [
        {
            "input": {
                "differences": [1, -3, 4],
                "lower": 1,
                "upper": 6
            },
            "output": 2
        },
        {
            "input": {
                "differences": [3,-4,5,1,-2],
                "lower": -4,
                "upper":5 
            },
            "output": 4
        },
        {
            "input": {
                "differences": [4,-7,2],
                "lower": 3, 
                "upper":6
            },
            "output": 0
        }
    ]
    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["output"]
        result = Solution().numberOfArrays(**input_data)
        print(f"Test case {i + 1} : expected {expected_output}, got {result}")