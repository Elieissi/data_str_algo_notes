class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for a in s:
            if a.isalnum():
                cleaned += a.lower()
        
        return cleaned == cleaned[::-1]