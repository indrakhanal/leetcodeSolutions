class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_list = s.split(' ')
        count = 0
        for i in reversed(string_list):
            if len(i)>0:
                count = len(i)
                break
        return count
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = 0
        for i, num in enumerate(nums):
            if num == target:
                idx = i
                break
            else:
                if(num<target):
                    idx = i+1
        return idx
                

obj = Solution()
out = obj.searchInsert([1,3,5,6], 5)
print(out)