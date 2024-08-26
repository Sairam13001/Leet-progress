class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums[i+1:])):
        #         if (nums[i]+nums[i+j+1] == target):
        #             return [i,i+j+1]

        # b = list(enumerate(nums))
        # c = sorted(b, key = lambda x:x[1])
        # sorted_nums = [element for index, element in c]
        # sorted_inds = [index for index, element in c]
        # start = 0; end = len(nums) - 1
        # while(True):
        #     if (sorted_nums[start] + sorted_nums[end] == target):
        #         return [sorted_inds[start], sorted_inds[end]]
        #     elif(sorted_nums[start] + sorted_nums[end] < target):
        #         start += 1
        #     else:
        #         end -= 1

        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i

        