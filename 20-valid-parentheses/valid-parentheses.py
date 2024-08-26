class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # p = {"(":")", "[":"]", "{":"}"}
        # if len(s)<2:
        #     return False
        # a = list(s)
        # b = []
        # while (len(a)>0):
        #     if len(b) == 0:
        #         b.insert(0, a.pop())
        #     elif (a[-1] in p.keys()) and (p[a[-1]] == b[0]):
        #         a.pop()
        #         b.pop(0)
        #     else:
        #         b.insert(0, a.pop())
        # return len(b) == 0

        p = {")":"(", "]":"[", "}":"{"}
        q = []
        for c in s:
            if c not in p:
                q.append(c)
                continue
            if not q or p[c] != q[-1]:
                return False
            q.pop()
        return not q




