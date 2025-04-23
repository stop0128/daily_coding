class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        return
    
if __name__ == "__main__":
    test_cases = [
        {
            "input": {
                "n": 2,
                "maxValue": 5
            },
            "output": 10
        },
        {
            "input": {
                "n": 5,
                "maxValue": 3
            },
            "output": 11
        },
    ]
    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["output"]
        result = Solution().idealArrays(**input_data)
        print(f"Test case {i + 1} : expected {expected_output}, got {result}")
    ]