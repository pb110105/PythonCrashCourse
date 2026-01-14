class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i1 = len(nums)
        j1 = len(nums)-1
        for i in range(i1):
            for j in range(0, j1):
                if nums[i] == nums[j]:
                    nums.pop(j)
            break
        return len(nums), nums
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))