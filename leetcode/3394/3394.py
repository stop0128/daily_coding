from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_divide_into_three_segments(segments: List[List[int]]) -> bool:
            segments.sort()
        
            section = 0
            max_end = segments[0][1]
        
            for start, end in segments:
                if start >= max_end:
                    section += 1
                max_end = max(max_end, end)
                
            if section >= 2:
                return True
            else:
                return False
            
        xs = [[rectangle[0], rectangle[2]] for rectangle in rectangles]
        ys = [[rectangle[1], rectangle[3]] for rectangle in rectangles]
                
        return can_divide_into_three_segments(xs) or can_divide_into_three_segments(ys)
    

if __name__ == "__main__":
    test_cases = [
        {
            "n": 5,
            "rectangles": [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]], 
            "expected": True
        },
        {
            "n": 4,
            "rectangles": [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]], 
            "expected": True
        },
        {
            "n": 4,
            "rectangles": [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]], 
            "expected": False
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        n = test_case.get("n")
        rectangles = test_case.get("rectangles")
        expected = test_case.get("expected")
        result = solution.checkValidCuts(n, rectangles)
        print(result, expected)