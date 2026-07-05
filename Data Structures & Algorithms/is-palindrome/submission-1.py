class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [
            x 
            for x in s 
            if (
                (x >= 'a' and x <= 'z')
                 or 
                (x >= '0' and x <= '9')
            )
            ]
        return s == s[::-1]
        