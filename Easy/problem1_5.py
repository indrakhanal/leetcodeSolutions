class Solution:
    def twoSum(self, nums, target: int):
        numToIndex = {}

        for i, num in enumerate(nums):
            # print(i, num, numToIndex)
            if target - num in numToIndex:
                return numToIndex[target - num], i
            numToIndex[num] = i
            
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key_value = {"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        arr_item = [*s]
        output = 0
        for i in range(len(arr_item) - 1):
            if key_value[arr_item[i]] < key_value[arr_item[i + 1]]:
                output -= key_value[arr_item[i]]
            else:
                output += key_value[arr_item[i]]
        output += key_value[arr_item[-1]]
        return output
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        open_list = ["(", "{", "["]
        close_list = [")","}","]"]
        stack_list = []
        for i in s:
            if i in open_list:
                stack_list.append(i)
            elif i in close_list:
                close_pos = close_list.index(i)
                if len(stack_list) > 0 and open_list[close_pos] == stack_list[len(stack_list)-1]:
                    stack_list.pop()
                else:
                    return False
        if len(stack_list) == 0:
            return True
        else:
            return False
        
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node_list = ListNode(0)
        current_list = node_list
        while list1 and list2:
            if list1.val < list2.val:
                current_list.next = list2 
                list1  = list1.next
            else:
                current_list.next = list2
                list2 = list2.next
            current_list = current_list.next
        current_list.next = list1 or list2
        return node_list.next
      
obj = Solution()
t = obj.mergeTwoLists([1,2,3], [1,4,5])
print(t)

