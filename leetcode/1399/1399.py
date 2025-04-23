class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(n: int) -> int:
            ns = str(n)
            result = 0
            for c in ns:
                result += int(c)
            return result
        groups = [[]]
        for c in range(1, n+1):
            sum_c = sum_digits(c)
            if len(groups) < sum_c:
                groups.append([c])
            else:
                groups[sum_c-1].append(c)
        
        max_value = 0
        max_len = 0
        for group in groups:
            if len(group) > max_len:
                max_len = len(group)
                max_value = 1
            elif len(group) == max_len:
                max_value += 1
                
        return max_value
    
if __name__ == "__main__":
    test_cases = [
        {
            "n": 13,
            "output": 4
        },
        {
            "n": 2,
            "output": 2
        },
        {
            "n": 15,
            "output": 6
        }
    ]
    for i, test_case in enumerate(test_cases):
        n = test_case["n"]
        expected_output = test_case["output"]
        result = Solution().countLargestGroup(n)
        print(f"Test case {i + 1} : expected {expected_output}, got {result}")