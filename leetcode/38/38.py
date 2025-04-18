class Solution:
    def countAndSay(self, n: int) -> str:
        def get_RLE(n: str) -> str:
            if n == 1:
                return "1"
            
            m = len(n)
            c = n[0]
            
            count, result = 0, ""
            
            for i in range(m):
                if c == n[i]:
                    count += 1
                else:
                    result = result + f"{count}{n[i-1]}"
                    c = n[i]
                    count = 1
            else:
                result = result + f"{count}{n[i]}"
            
            return result

        ret = get_RLE(1)
        for i in range(n-1):
            ret = get_RLE(ret)
            
        return ret

if __name__ == "__main__":
    test_cases =[
        {
            "n": 1,
            "expected": "1"
        },
        {
            "n": 2,
            "expected": "11"
        },
        {
            "n": 3,
            "expected": "21"
        },
        {
            "n": 4,
            "expected": "1211"
        }
    ]
    
    for test_case in test_cases:
        n = test_case["n"]
        expected = test_case["expected"]
        
        solution = Solution()
        result = solution.countAndSay(n)
        print(f"Input: {n}, Expected: {expected}, Result: {result}")