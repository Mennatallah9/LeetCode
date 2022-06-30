class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        result = []
        for word in words:
            if word[len(word)::-1] == word:
                result.append(word)
                break
        return " ".join(result)
