class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s = []
        letter_t = []
        for letter in s:
            letter_s.append(letter)
        
        for letters in t:
            letter_t.append(letters)
        
        if sorted(letter_s) == sorted(letter_t):
            return True
        else:
            return False