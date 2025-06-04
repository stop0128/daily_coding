class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        max_char = max(word)
        length = n - numFriends + 1
        result = ""

        for i in range(n):
            if word[i] == max_char:
                substr = word[i:i + length]
                result = max(result, substr)

        return result