class Solution(object):
    def isPalindrome(self, s):
        j = len(s) - 1
        i = 0
        s = s.lower()
        while i < j:
            if not(s[i].isalpha()):
                i += 1
                continue
            if not(s[j].isalpha()):
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

        """
        :type s: str
        :rtype: bool
        """
        