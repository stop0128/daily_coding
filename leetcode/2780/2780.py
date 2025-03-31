from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def get_dominant(nums: List[int]) -> int:
            table = {}
            
            if len(nums) == 0:
                return -1
            
            for num in nums:
                if table.get(num) == None:
                    table[num] = 0
                table[num] += 1

            max_key = max(table, key=table.get)
            
            if table[max_key] > (len(nums) // 2):
                return max_key
            
            return -1

        nums_dominant = get_dominant(nums)
        if nums_dominant == -1:
            return -1
        
        nums_dominant_count = nums.count(nums_dominant)
        
        left_count, right_count = 0, nums_dominant_count
        
        for i in range(len(nums) - 1):
            if nums[i] == nums_dominant:
                left_count += 1
            right_count = nums_dominant_count - left_count
            
            if (left_count > ((i + 1)// 2)) and (right_count > (len(nums) - (i + 1)) // 2):
                return i
        
        return -1
        
if __name__ == "__main__":
    test_cases = [
        {
            "nums": [1,2,2,2],
            "expected": 2
        },
        {
            "nums": [2,1,3,1,1,1,7,1,2,1],
            "expected": 4
        },
        {
            "nums": [3,3,3,3,7,2,2],
            "expected": -1
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        nums = test_case.get("nums")
        expected = test_case.get("expected")
        result = solution.minimumIndex(nums)
        print(result, expected)