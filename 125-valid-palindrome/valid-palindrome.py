class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [i.lower() for i in s if i.isalnum()]
        return a == a[::-1]