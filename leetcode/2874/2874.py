from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        high, diff, ans = 0, 0, 0
        
        for num in nums:
            ans = max(ans, diff * num)
            
            diff = max(high - num, diff)
            
            high = max(high, num)
            
        return ans
    
if __name__ == "__main__":
    test_cases = [
        {
            "nums": [12,6,1,2,7], 
            "expected": 77
        },
        {
            "nums": [1,10,3,4,19], 
            "expected": 133
        },
        {
            "nums": [1,2,3], 
            "expected": 0
        },
        {
            "nums": [2,3,1], 
            "expected": 0
        },
        {
            "nums": [6,11,12,12,7,9,2,11,12,4,19,14,16,8,16],
            "expected": 190
        },
        {
            "nums": [13,4,3,19,16,14,17,6,20,6,16,4],
            "expected": 260
        },
        {
            "nums": [15,3,3,18,19,13,7,5,18,1,8,5],
            "expected": 252
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        nums = test_case.get("nums")
        expected = test_case.get("expected")
        result = solution.maximumTripletValue(nums)
        print(result, expected)