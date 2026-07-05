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
        forward = []
        reverse = []
        n = len(s)
        flag = True
        for i in range(n):
            if s[i] != s[n-i-1]:
                return False


        return flag
        