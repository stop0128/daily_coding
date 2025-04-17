class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        n = len(s)
        result = 0
                
        left_finish_s = str(finish)[:-n]
        left_start_s = str(start)[:-n]
        
        if not len(left_start_s):
            start_n = 1
        else:
            start_n = int(left_start_s)
            
        if not len(left_finish_s):
            return 0
        left_finish = int(left_finish_s)
        
        if int(str(finish)[-n:]) >= int(s):
            result += 1
        
        for i in range(start_n, left_finish):
            s_i = str(i)
            for c in s_i:
                if int(c) > limit:
                    break
            else:
                result +=1
                        
        return result
    

if __name__ == "__main__":
    test_cases = [
        {
            "start": 1,
            "finish": 6000,
            "limit": 4,
            "s": "124",
            "expected": 5
        },
        {
            "start": 15,
            "finish": 215,
            "limit": 6,
            "s": "10",
            "expected": 2
        },
        {
            "start": 1000,
            "finish": 2000,
            "limit": 4,
            "s": "3000",
            "expected": 0
        },
        {
            "start": 1,
            "finish": 971,
            "limit": 9,
            "s": "71",
            "expected": 10
        },
        {
            "start": 141,
            "finish": 148,
            "limit": 9,
            "s": "9",
            "expected": 0
        },
        {
            "start": 1,
            "finish": 971,
            "limit": 9,
            "s": "17",
            "expected": 10
        },
        {
            "start": 1829505,
            "finish": 1255574165,
            "limit": 7,
            "s": "11223",
            "expected": 5470
        }
    ]
    solution = Solution()
    for test_case in test_cases:
        start = test_case.get("start")
        finish = test_case.get("finish")
        limit = test_case.get("limit")
        s = test_case.get("s")
        expected = test_case.get("expected")
        result = solution.numberOfPowerfulInt(start, finish, limit, s)
        print(result, expected)