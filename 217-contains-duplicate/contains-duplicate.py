class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(nums) != len(set(nums))
        a = set()
        for n in nums:
            if n in a:
                return True
            a.add(n)
        return False

            
        