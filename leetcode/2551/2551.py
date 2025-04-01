from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if (k == 1) or (k >= len(weights) - 1):
            return 0
        
        sub_weights = []
        
        for i in range(len(weights)):
            
        
        return
    
    
if __name__ == "__main__":
    test_cases = [
        {
            "weights": [1,3,5,1],
            "k": 2, 
            "expected": 4
        },
        {
            "weights": [1,3],
            "k": 2, 
            "expected": 0
        },
        {
            "weights": [1,2,3,4,5],
            "k": 3, 
            "expected": 4
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        weights = test_case.get("weights")
        k = test_case.get("k")
        expected = test_case.get("expected")
        result = solution.putMarbles(weights, k)
        print(result, expected)