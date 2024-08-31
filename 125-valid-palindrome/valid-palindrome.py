class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [i.lower() for i in s if i.isalnum()]
        return a == a[::-1]

        # new = ''
        # for a in s:
        #     if a.isalnum():
        #         new += a.lower()
        # return (new == new[::-1])

        # if not s:
        #     return True
        
        # start = 0
        # last = len(s) - 1
        
        # while start <= last:
        #     currFirst = s[start]
        #     currLast = s[last]
            
        #     if not currFirst.isalnum():
        #         start += 1
        #     elif not currLast.isalnum():
        #         last -= 1
        #     else:
        #         if currFirst.lower() != currLast.lower():
        #             return False
        #         start += 1
        #         last -= 1
        
        # return True