class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = {")":"(", "]":"[", "}":"{"}
        l = [letter for letter in s]
        if len(l) == 1:
            return False
        k = []
        while(len(l)>0):
            if len(k) == 0:
                k.append(l.pop())
            if (k[-1] in p.keys()) and (len(l)>0):
                if (p[k[-1]] == l[-1]):
                    k.pop()
                    l.pop()
                else:
                    k.append(l.pop())
            else:
                return False
        if (len(l) == 0) and (len(k) == 0):
            return True
        else:
            return False


