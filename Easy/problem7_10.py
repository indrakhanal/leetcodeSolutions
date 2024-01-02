class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                print(nums[i-1])
                nums[count] = nums[i]
                count+=1
        return count
        
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1
            
        # print(nums, "==")
        return count
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryover = 0
        list3 = []
        if len(l1) != len(l2):
            for i in range(len(l1)):
                if (i>=len(l2)):
                    l2.append(0)
        for i in range(len(l1)):
            if(l1[i]+l2[i] +carryover >=10):
                temp = l1[i]+l2[i]+carryover-10
                list3.append(temp)
                carryover = 1
                if i+1 == len(l1):
                    list3.append(carryover)
            else:
                list3.append(l1[i]+l2[i]+carryover)
                carryover = 0
        return list3
            
            
obj = Solution()
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
v = obj.addTwoNumbers(l1, l2)
print("solution is:", v)
