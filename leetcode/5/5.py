class Solution:
    def longestPalindrome(self, s: str) -> str:
        def reverse_s(s: str):
            return s[::-1]
        
        len_s = len(s)
        max_p = s[0]
    
        for i in range(0, len_s + 1):
            for j in range(i + 1, len_s + 1):
                os = s[i:j]
                rs = reverse_s(os)
                if (os == rs) and (len(max_p) < len(rs)):
                    max_p = os
        
        return max_p
        
            
if __name__ == "__main__":
    test_cases = [
        {
            "s": "babad",
            "expected": "bab"
        },
        {
            "s": "cbbd",
            "expected": "bb"
        },
        {
            "s": "bb",
            "expected": "bb"
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        s = test_case.get("s")
        expected = test_case.get("expected")
        result = solution.longestPalindrome(s)
        print(result, expected)