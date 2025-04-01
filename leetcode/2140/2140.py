from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  #문제 풀경우와 아닌경우
        
        for i in range(n - 1, -1, -1):
            point, brainpower = questions[i]
            next_question = i + brainpower + 1
            
            if next_question < n:
                dp[i] = max(dp[i+1], point + dp[next_question])
            else:
                dp[i] = max(dp[i+1], point)
            
        return dp[0]
            
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