class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def check_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        n = len(s)
        dp = [0] * n
        dp[0] = s[0]
        
        for i in range(1, n):
            sum_s = dp[i-1]+s[i]
            bef_s = dp[i-1]
            now_s = s[i]
            
            palindromes = [p for p in [sum_s, bef_s, now_s] if check_palindrome(p)]
            print(f"sum_s {sum_s} bef_s {bef_s} now_s {now_s}")
            if not palindromes:
                dp[i] = now_s
            else:
                dp[i] = max(palindromes, key=len)
            
            print(dp)
        return
        
        
        

if __name__ == "__main__":
    test_cases = [
        {
            "s": "bbbab", 
            "expected": "bbbb"
        },
        {
            "s": "cbbd", 
            "expected": "bb"
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        s = test_case.get("s")
        expected = test_case.get("expected")
        result = solution.longestPalindromeSubseq(s)
        print(result, expected)