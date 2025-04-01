from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def get_max_points(questions: List[List[int]]) -> int:
            len_questions = len(questions)
            points = [0] * len_questions
            if len_questions == 0:
                return 0
            
            for i in range(len_questions):
                points[i] += questions[i][0]
                points[i] += get_max_points(questions[questions[i][1]+i+1:])
            
            return max(points)
    
        return get_max_points(questions)
        
if __name__ == "__main__":
    test_cases = [
        {
            "questions": [[3,2],[4,3],[4,4],[2,5]],
            "expected": 5
        },
        {
            "questions": [[1,1],[2,2],[3,3],[4,4],[5,5]],
            "expected": 7
        },
        {
            # 92 + 65
            "questions": [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]],
            "expected": 157
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        questions = test_case.get("questions")
        expected = test_case.get("expected")
        result = solution.mostPoints(questions)
        print(result, expected)