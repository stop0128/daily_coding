from typing import List

class Solution:
    def can_divide_into_three_segments(self, segments: List[List[int]]) -> bool:
        segments.sort()
        
        points = sorted(set(start for start, end in segments) | set (end for start, end in segments))
        
        for i in range(1, len(points) - 1):
            for j in range(i + 1, len(points)):
                cut1, cut2 = points[i], points[j]
                
                group1, group2, group3 = False, False, False
                
                for start, end in segments:
                    if end <= cut1:
                        group1 = True
                    elif start >= cut2:
                        group3 = True
                    elif start >= cut1 and end <= cut2:
                        group2 = True
                    else:
                        break
                else:
                    if group1 and group2 and group3:
                        return True
        
        return False
                
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs = []
        ys = []
        
        for rectangle in rectangles:
            xs.append([rectangle[0], rectangle[2]])
        
        if self.can_divide_into_three_segments(xs):
            return True
        
        for rectangle in rectangles:
            ys.append([rectangle[1], rectangle[3]])
            
        if self.can_divide_into_three_segments(ys):
            return True
        
        return False
    

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